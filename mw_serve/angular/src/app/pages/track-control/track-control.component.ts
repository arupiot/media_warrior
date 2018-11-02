import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { GetTracksService } from '../services/get-tracks.service';
import { of, Observable } from 'rxjs';

@Component({
  selector: 'app-track-control',
  templateUrl: './track-control.component.html',
  styleUrls: ['./track-control.component.css']
})
export class TrackControlComponent implements OnInit {

  serverData: Observable<any>;
  errorResponse = '';
  id: number;
  private sub: any;
  

  constructor(private route: ActivatedRoute, 
              private getTracksService: GetTracksService
              ) { }
  

  ngOnInit() 
  {    
    this.sub = this.route.params.subscribe(params => 
      {
        this.id = +(params['id']);
      })
    this.getTracksService.getSingleTrack(this.id).subscribe(
      (data: any) => {
        console.log('from service: ', data);
        this.serverData = of(data);
      },
      (err: any) => {
        console.log("error", err);
        this.errorResponse = err;
      }
    )
  }
  playMusic()
  {
    this.getTracksService.playSingleTrack(this.id).subscribe(
      (data) =>{
        console.log(data);
      }
      );
  }
}

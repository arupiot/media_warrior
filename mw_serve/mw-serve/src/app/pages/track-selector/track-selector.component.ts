import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { of, Observable } from 'rxjs';
import { GetTracksService } from '../services/get-tracks.service';

@Component({
  selector: 'app-track-selector',
  templateUrl: './track-selector.component.html',
  styleUrls: ['./track-selector.component.css']
})
export class TrackSelectorComponent implements OnInit {
  title = 'mw_serve';
  serverData: Observable<any>;
  errorResponse = '';

  constructor(
              private httpClient: HttpClient,
              private getTracksService: GetTracksService
              ) {
  }


  styleObject() {
    return{
      // border: 'none',
     };
 }

 itemStyleObject() {
   return {
    // border: '0.1em solid white',
    // marginBottom: '2em',
    // background: 'black'
   };
 }
  ngOnInit () {
    // console.log(window.location.hostname);

    this.getTracksService.getTracks().subscribe(
      (data: any) => {
        console.log('from service: ', data);
        this.serverData = of(data);
      },
      (err: any) => {
        console.log('error', err);
        this.errorResponse = err;
      }
    );
  }
}

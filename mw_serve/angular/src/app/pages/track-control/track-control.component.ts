import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { GetTracksService } from '../services/get-tracks.service';
import { of, Observable } from 'rxjs';
import { GetStylesService } from '../services/get-styles.service';

@Component({
  selector: 'app-track-control',
  templateUrl: './track-control.component.html',
  styleUrls: ['./track-control.component.css']
})
export class TrackControlComponent implements OnInit {
  serverData: Observable<any>;
  errorResponse = '';
  id: string;
  private sub: any;
  playing = false;

  constructor(
    private route: ActivatedRoute,
    private getTracksService: GetTracksService,
    private getStylesService: GetStylesService
  ) {}

  styleObject() {
    if (!this.getStylesService.getStyles()) {
      return {
        background: 'black',
        border: '0.2rem solid white'
      };
    }
  }

  styleObjectBorder() {
    if (!this.getStylesService.getStyles()) {
    return {
      border: 'none'
    };
  }
  }
  ngOnInit() {

    this.sub = this.route.params.subscribe(params => {
      this.id = params['id'];
    });
    this.getTracksService.getSingleTrack(this.id).subscribe(
      (data: any) => {
        console.log('from (singelTrack) service: ', data);
        this.serverData = of(data.slice(0, data.length - 4));
      },
      (err: any) => {
        console.log('error', err);
        this.errorResponse = err;
      }
    );
  }

  playMusic() {
    this.playing = !this.playing;
    this.getTracksService.playSingleTrack(this.id).subscribe(data => {
      console.log(data);
    });
  }

  pauseMusic() {
    this.playing = !this.playing;
    console.log(this.playing);
    this.getTracksService.pauseSingleTrack(this.id).subscribe(data => {
      console.log(data);
    });
  }

  stopMusic() {
    this.getTracksService.stopMusic().subscribe(data => {
      console.log(data);
    });
    this.playing = false;
  }
}

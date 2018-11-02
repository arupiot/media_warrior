import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { of, Observable } from 'rxjs';
import { GetTracksService } from '../services/get-tracks.service';
import { GetStylesService } from '../services/get-styles.service';


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
              private getTracksService: GetTracksService,
              private getStylesService: GetStylesService
              ) {
  }


  styleObject() {
    if (!this.getStylesService.getStyles()) {
      return{
        border: 'none',
        paddingTop: '1.6rem'
       };
    }
 }

 itemStyleObject() {
  if (!this.getStylesService.getStyles()) {
   return {
    border: '0.2rem solid white',
    background: 'black',
    marginTop: '0.4em',
    marginBottom: '0.4em'
   };
 }
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

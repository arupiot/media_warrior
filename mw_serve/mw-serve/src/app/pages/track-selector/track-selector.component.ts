import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-track-selector',
  templateUrl: './track-selector.component.html',
  styleUrls: ['./track-selector.component.css']
})
export class TrackSelectorComponent implements OnInit {
  title = 'mw_serve';
  serverData: JSON = null;
  errorResponse = '';

  constructor(private httpClient: HttpClient) {
  }

  ngOnInit () {
    // console.log(window.location.hostname);

    this.httpClient.get('http://' + window.location.hostname + ':5002/get-track-list').subscribe(
      data => {
      this.serverData = data as JSON;
      console.log('Synced tracks: ', data);
      },
      err => {
        this.errorResponse = err;
        console.log(this.errorResponse);
      }
    );
  }
}

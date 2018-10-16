import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-track-control',
  templateUrl: './track-control.component.html',
  styleUrls: ['./track-control.component.css']
})
export class TrackControlComponent implements OnInit {

  serverData: JSON = null;
  errorResponse = '';

  constructor(private httpClient: HttpClient) { }

  ngOnInit() {
  }

  onPlayClicked() {
    this.httpClient.get('http://127.0.0.1:5002/play').subscribe(data => {
      this.serverData = data as JSON;
      console.log(this.serverData);
    });
  }

  onStopClicked() {
    this.httpClient.get('http://127.0.0.1:5002/stop').subscribe(data => {
      this.serverData = data as JSON;
      console.log(this.serverData);
    });
  }

}

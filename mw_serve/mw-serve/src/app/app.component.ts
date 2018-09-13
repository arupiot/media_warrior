import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'mw_serve';
  serverData: JSON;

  constructor(private httpClient: HttpClient) {
  }

  ngOnInit () {
    this.httpClient.get('http://127.0.0.1:5002/get-track-list').subscribe(data => {
      this.serverData = data as JSON;
      console.log(this.serverData);
    });
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

import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-track-control',
  templateUrl: './track-control.component.html',
  styleUrls: ['./track-control.component.css']
})
export class TrackControlComponent implements OnInit {

  serverData: JSON = null;
  errorResponse = '';
  id: number;
  private sub: any;
  

  constructor(private route: ActivatedRoute, 
              private httpClient: HttpClient
              ) { }

  ngOnInit() 
  {
    this.httpClient.get('http://127.0.0.1:5002/get-track-list').subscribe(
      data => {
      this.serverData = data as JSON;
      console.log('Synced tracks: ', data);
      },
      err => {
        this.errorResponse = err;
        console.log(this.errorResponse);
      }
    );

    this.sub = this.route.params.subscribe(params => {
      this.id = +(params['id']);
    })
    console.log(this.id);    
  }
}

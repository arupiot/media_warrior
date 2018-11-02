import { Component, OnInit } from '@angular/core';
import { GetTracksService } from '../services/get-tracks.service';

@Component({
  selector: 'app-splash-screen',
  templateUrl: './splash-screen.component.html',
  styleUrls: ['./splash-screen.component.css']
})
export class SplashScreenComponent implements OnInit {

  constructor(private getTracksService: GetTracksService) { }

  ngOnInit() {
  }
}

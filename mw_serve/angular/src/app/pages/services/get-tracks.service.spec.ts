import { TestBed, inject } from '@angular/core/testing';

import { GetTracksService } from './get-tracks.service';

describe('GetTracksService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GetTracksService]
    });
  });

  it('should be created', inject([GetTracksService], (service: GetTracksService) => {
    expect(service).toBeTruthy();
  }));
});

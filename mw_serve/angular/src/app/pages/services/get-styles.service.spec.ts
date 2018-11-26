import { TestBed, inject } from '@angular/core/testing';

import { GetStylesService } from './get-styles.service';

describe('GetStylesService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GetStylesService]
    });
  });

  it('should be created', inject([GetStylesService], (service: GetStylesService) => {
    expect(service).toBeTruthy();
  }));
});

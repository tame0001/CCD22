import { TestBed } from '@angular/core/testing';

import { FieldOperationService } from './field-operation.service';

describe('FieldOperationService', () => {
  let service: FieldOperationService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FieldOperationService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { FieldOperationData } from './app.component';

@Injectable({
  providedIn: 'root'
})
export class FieldOperationService {

  private url = 'http://localhost:5000/field_operation';
  constructor(private http: HttpClient) { }

  getData(){
    return this.http.get<FieldOperationData[]>(this.url);
  }
}

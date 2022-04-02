import { Component, OnInit } from '@angular/core';
import { FieldOperationService } from './field-operation.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'frontend';
  rawData: FieldOperationData[] = [];
  allData: FieldOperationData[] = [];
  constructor(private service: FieldOperationService) {}

  ngOnInit() {
    this.service.getData()
      .subscribe(Response => {
        this.allData = Response;
        console.log(this.allData);
        this.allData.forEach((data: FieldOperationData) => {
          data.time = new Date(data.time);
          console.log(data);
        });
      });
  }
}

export interface FieldOperationData {
  field: string;
  operation: string;
  time: Date;
  detail: string;
}

import { Chart } from 'angular-highcharts';
import { Component, Input, OnInit } from '@angular/core';
import { DataService } from 'src/app/services/data.service';

@Component({
  selector: 'app-highchart',
  templateUrl: './highchart.component.html',
  styleUrls: ['./highchart.component.scss'],
})
export class HighchartComponent implements OnInit {
  @Input() uuid!: string;
  data: any;
  constructor(private dataService: DataService) {}

  ngOnInit(): void {
    this.data = new Chart(
      this.dataService.highchart_data.get(this.uuid)?.config as any
    );
  }
}

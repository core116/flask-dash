import { Component, Input, OnInit } from '@angular/core';
import { UntypedFormControl } from '@angular/forms';
import { MEData, ResponseData } from 'src/app/shared/application_data';

import { ViewChild } from '@angular/core';

import { MatSelect } from '@angular/material/select';
import { Observable, ReplaySubject, Subject, Subscription } from 'rxjs';
import {
  debounceTime,
  filter,
  map,
  take,
  takeUntil,
  tap,
} from 'rxjs/operators';
import { DataService } from 'src/app/services/data.service';
import { CallServiceService } from 'src/app/services/call-service.service';

@Component({
  selector: 'app-simple-filter',
  templateUrl: './simple-filter.component.html',
  styleUrls: ['./simple-filter.component.scss'],
})
export class SimpleFilterComponent implements OnInit {
  @Input() uuid!: string;
  dataForm = new UntypedFormControl();
  multi!: boolean;

  data: string[] | undefined;
  dataUrl: string | undefined;
  dataCall: Subscription | undefined;
  compareFn = (a:any, b:any) => a && b && a.id === b.id;


  public data_select_control: UntypedFormControl = new UntypedFormControl();

  /** control for the MatSelect filter keyword multi-selection */
  public data_search_control: UntypedFormControl = new UntypedFormControl();

  /** list of banks filtered by search keyword */
  public data_search: ReplaySubject<string[]> = new ReplaySubject<string[]>(1);
  public searching = false;

  @ViewChild('dataSelect', { static: true }) dataSelect!: MatSelect;
  /** Subject that emits when the component has been destroyed. */
  protected _onDestroy = new Subject<void>();



  constructor(
    private dataService: DataService,
    private callService: CallServiceService
  ) {}

  ngOnInit(): void {
    this.originalData();
    this.searchOrPullData();

    if (this.dataService.simple_filter_data.get(this.uuid)?.url !== undefined) {
      this.pullData();
    }
  }

  ngAfterViewInit() {}

  ngOnDestroy() {
    this._onDestroy.next();
    this._onDestroy.complete();
  }

  protected setInitialValue() {
    this.data_search.pipe(take(1), takeUntil(this._onDestroy)).subscribe(() => {
      this.dataSelect.compareWith = (a: string, b: string) => a === b;
    });
  }

  protected filterMulti() {
    if (!this.data) {
      return;
    }
    // get the search keyword
    let search = this.data_search_control.value;
    if (!search) {
      this.data_search.next(this.data.slice());
      return;
    } else {
      search = search.toLowerCase();
    }
    // filter the banks
    this.data_search.next(
      this.data.filter((data) => data.toLowerCase().indexOf(search) > -1)
    );
  }

  originalData() {
    this.dataUrl = this.dataService.simple_filter_data.get(this.uuid)?.url;
    this.multi = this.dataService.simple_filter_data.get(this.uuid)
      ?.multi as boolean;

    this.data = this.dataService.simple_filter_data.get(this.uuid)
      ?.data as string[];

    // set initial selection
    this.data_select_control.setValue([]);

    // load the initial bank list
    this.data_search.next(this.data.slice());
  }

  searchData() {
    this.data_search_control.valueChanges
      .pipe(takeUntil(this._onDestroy))
      .subscribe(() => {
        this.filterMulti();
      });

    this.setInitialValue();
  }

  pullData() {
    if (this.dataCall !== undefined) {
      this.dataCall.unsubscribe();
    }

    this.data_search_control.valueChanges.subscribe((search) => {
      if (search === '') {
        return;
      }
      let p = this.callService.second_call_response(
        location.origin + this.dataUrl,
        (this.dataService.simple_filter_data.get(this.uuid)?.name as string) +
          '_search',
        search as string
      );

      this.dataCall = p.subscribe((data) => {
        let fi = data.simple_fitler_data as string[];
        this.searching = false;
        this.data_search.next(fi);
      });


    });

  }

  searchOrPullData() {
    // listen for search field value changes
    if (this.dataService.simple_filter_data.get(this.uuid)?.url !== undefined) {
      // this.pullData();
    } else {
      this.searchData();
    }
  }

  getLabel() {
    return this.dataService.simple_filter_data.get(this.uuid)?.name;
  }

  detectChange(value: any) {
    let m = new MEData();
    m.key = this.dataService.simple_filter_data.get(this.uuid)?.name as string;
    m.value = value.value;

    this.dataService.data_setter.emit(m);
  }

  isServerSide(){
    return this.dataUrl !== undefined
  }
}

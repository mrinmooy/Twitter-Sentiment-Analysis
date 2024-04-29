import { Routes } from '@angular/router';

import {SendTweetsComponent} from './components/send-tweets/send-tweets.component'
import {PositiveComponent} from './components/postive/postive.component'
import {NegativeComponent} from './components/negative/negative.component'



export const routes: Routes = [
    {
        path: '',
        redirectTo: 'sendtweets',
        pathMatch: 'full'
    },
    {
        path: 'sendtweets',
        component: SendTweetsComponent
    },
    {
        path: 'positive',
        component: PositiveComponent
    },
    {
        path: 'negative',
        component: NegativeComponent
    }
];

import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {ComposantJoueurComponent} from "./composant-joueur/composant-joueur.component";
import {HttpClientModule} from "@angular/common/http";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, ComposantJoueurComponent,HttpClientModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'front-pingpong';
}

import { Routes } from '@angular/router';
import {ComposantJoueurComponent} from "./composant-joueur/composant-joueur.component";
import {AjouterJoueurComponent} from "./ajouter-joueur/ajouter-joueur.component";

export const routes: Routes = [
  {path:'joueurs', component:ComposantJoueurComponent},
  {path:'addJ', component:AjouterJoueurComponent}

];


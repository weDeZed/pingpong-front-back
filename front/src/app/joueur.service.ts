import { Injectable,inject } from '@angular/core';
import { HttpClient } from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class JoueurService {

  private http = inject(HttpClient)


  constructor() {}
  getJoueurs(){
    return this.http.get('/api/liste_joueurs');
    }


  addJoueur(joueurJSON: JSON){
    return this.http.post<JSON>('http://127.0.0.1:5000/ajouter_joueur',joueurJSON);
  }



}

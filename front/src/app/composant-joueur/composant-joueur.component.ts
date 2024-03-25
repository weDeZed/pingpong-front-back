import {Component,inject, OnInit} from '@angular/core';
import {JoueurService} from "../joueur.service";
import {NgFor} from "@angular/common";

@Component({
  selector: 'app-composant-joueur',
  standalone: true,
  imports: [NgFor],
  templateUrl: './composant-joueur.component.html',
  styleUrls: ['./composant-joueur.component.css']
})
export class ComposantJoueurComponent implements OnInit {

  private joueurService = inject(JoueurService);
  joueurs: any= [];

  ngOnInit(): void {
    this.loadPosts();
  }


  loadPosts(){
    this.joueurService.getJoueurs().subscribe((joueurs : any) =>{
      console.log(joueurs);
      this.joueurs = joueurs;

    });
  }

}

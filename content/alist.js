//--------------------------------------
// WEB 2019/2020
// Aufgabe P2 / Anwendungsrahmen
//--------------------------------------
'use strict';

window.onload = function () {
   var el_o = document.querySelector("body");
   if (el_o !== null) {
      el_o.addEventListener("click", function (event_opl) {
         if (("action" in event_opl.target.dataset) &&
             ("id" in event_opl.target.dataset)        ) {
            switch (event_opl.target.dataset["action"]) {
               case "add":
                  window.location.href = "/abteilung/add/";
                  break;
               case "edit":
                  window.location.href = "/abteilung/edit/" + event_opl.target.dataset["id"];
                  break;
               case "delete":
                  if (confirm("Soll der Eintrag gelöscht werden?")) {
                     window.location.href = "/abteilung/delete/" + event_opl.target.dataset["id"];
                  }
                  break;
            }
            event_opl.stopPropagation();
            event_opl.preventDefault();
         } else {
            console.warn("data-id oder data-action nicht gefunden");
         }
      });
   }
}
// EOF

//--------------------------------------
// WEB 2019/2020
// Aufgabe P2 / Anwendungsrahmen
//--------------------------------------
'use strict';

window.onload = function () {
   var el_o = document.querySelector("form");
   if (el_o !== null) {
      el_o.addEventListener("click", function (event_opl) {
         if ("action" in event_opl.target.dataset) {
            switch (event_opl.target.dataset["action"]) {
               case "save":
                  el_o.submit();
                  break;
               case "reset":
                  el_o.reset();
                  break;
               case "quit":
                  if (confirm("Soll die Bearbeitung beendet werden?")) {
                     window.location.href = "/employee/";
                  }
                  break;
            }
            event_opl.stopPropagation();
            event_opl.preventDefault();
         } else {
            console.warn("data-action nicht gefunden");
         }
      });
   }
}
// EOF
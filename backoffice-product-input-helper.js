/*
To easily run this script in the browser console without copying pasting the whole code, use the following command:
$.getScript("https://cdn.jsdelivr.net/gh/topcompare/tools/backoffice-product-input-helper.js")

You can/should load the data into the variable first:
var list = ... (for products)
var rt = ... (for results tables)
*/
console.log("Loading script version v0.1 20190321a");
// Declare the data list variable

switch($(".page-title").text()) {
  
  case "Credit Cards Edit Product":
    if (typeof list === "undefined") {
        if (confirm('There is no data list defined (var list = ...). Use the demo one?')) {
            console.log("Loading default data list");
            var list = { "CAFI0003": {"Columns": [["Online Aankoopverzekering", ""], ["Fraudeverzekering", "No"], ["Aankoopverzekering", "24090"], ["Uitbreiding van de garantie", ""], ["Reisongevallenverzekering", "150000"], ["Annuleringsverzekering", "7500"], ["Vertraging en gemiste vlucht verzekering", "750"], ["Bagageverzekering", "4375"], ["Bijstand aan voertuigen", "No"], ["Bijstand aan personen", "Yes"], ["Cashback", "No"], ["Voordelen", "Yes"], ["Kortingen", "Yes"], ["Kortingen", "Yes"], ["Miles", "No"], ["Toegang tot exclusieve lounges", "No"], ["Kaart limiet", "0"], ["Activatie kosten", "0"], ["Wisselend Tarief", "2.5"], ["Kosten geld opnamen (binnen de EU)", "4 + 0%"], ["Kosten geld opnamen (buiten de EU)", "5 + 0%"], ["Kosten voor extra kaart", "39"], ["Type kredietkaart", "credit"], ["Welkomstgeschenk", ""], ["Rentevoet", "12.49"], ["Jaarlijkse kosten", "39"], ["BethanyScoreVB", "1.64338703244651"], ["LaureenScoreVB", "1.95488873275292"], ["ArthurScoreVB", "3.15210613565224"], ["HailieScoreVB", "2.71840558202529"], ["ChadScoreVB", "1.89095816207758"], ["BethanyScoreVPB", "0.0410846758111629"], ["LaureenScoreVPB", "0.0488722183188231"], ["ArthurScoreVPB", "0.078802653391306"], ["HailieScoreVPB", "0.0679601395506323"], ["ChadScoreVPB", "0.0472739540519396"]],"Categories": [["Kortingen", true], ["Cashback", true]], "Sections": [["Section 1", "Hello world 1"], ["Section 2", "Hello second world"]],"Resultstbles":[["VB-Def_payments", true ],["VB-Basic_traveler", false]]}};
        } else {
            throw new Error("Need a valid data list to proceed!");
        }
    }
    
    var cggID = $("#cggId").val(); // Retrieve the product ID or the current page
    // Check if data list contains en entry for that cggID
    var lang = $(".translate-btn").text().trim();

    if (typeof list[cggID] !== "undefined") {
        // Columns: expects data pairs ["column_label", "column_value" ] in the "Columns" object of the list
        console.log("Entering the COLUMNS section.");
        for (var i = 0; i < list[cggID].Columns.length; i++) {
            //break;
            console.log("Setting " + list[cggID].Columns[i][0] + " to " + list[cggID].Columns[i][1] + "...");
            // find the correct line as a reference point based on the column label name
            var anchor_element = $("span.column-title").filter(function() {
                return $(this).text() == list[cggID].Columns[i][0];
            });
            var input_element = anchor_element.parent().siblings().eq(0).find("input");
            // set the value (and convert , to . because BO does not accept the float otherwise
            input_element.val(list[cggID].Columns[i][1].replace(/,/g, '.'));
            input_element.get(0).dispatchEvent(new Event('input'));

            if (typeof input_element.val() !== "undefined" && input_element.val() == list[cggID].Columns[i][1].replace(/,/g, '.')) {
                console.log("%c done", "color: green");
            } else {
                console.log("%c failed", "color: red");
            }
        }
        // Categories: expects data pairs ["category_label", true/false or 1/0 ] in the "Categories" object of the list
        console.log("Entering the CATEGORIES section.");
        for (var i = 0; i < list[cggID].Categories.length; i++) {
            //break;
            console.log("Setting " + list[cggID].Categories[i][0] + " to " + list[cggID].Categories[i][1] + "...");
            var anchor_element = $("category-partial span").filter(function() {
                return $(this).text() == list[cggID].Categories[i][0];
            });
            var input_element = anchor_element.parent().find("input");
            // set the value if object found
			if (input_element.length > 0) {
				input_element.prop( "checked", list[cggID].Categories[i][1]);
				input_element.get(0).dispatchEvent(new Event('change'));
			} else {
				console.log("%c Warning: field not found!", "color: grey");
			}
            if (typeof input_element.prop("checked") !== "undefined" && input_element.prop("checked") == list[cggID].Categories[i][1]) {
                console.log("%c done", "color: green");
            } else {
                console.log("%c failed", "color: red");
            }
        }
        // Sections: expects data pairs ["section_label", "free text / HTML"] in the "Sections" object of the list
        console.log("Entering SECTIONS of the More Info section. Current locale: "+ lang);
        for (var i = 0; i < list[cggID].Sections.length; i++) {
            console.log("Setting section "+i+ " out of "+ $(".more-info-input").length);
            var langClass = "."+lang;
            // Check if there are as many sections as in the datafile
            if (typeof $(".more-info-input").get(i) === "undefined"){
                if (confirm('There are not enough sections available. Create an additional one?')) {
                    console.log("Creating a new section...");
                    $("button").filter(function() {
                        return $(this).text() == " Add Section";
                    }).click();
                    // TODO: Confirm the new line has been created by testing the new element
                } else {
                    break;
                }
            }
            var anchor_element = $(".more-info-input").eq(i);
            var input_element_title = anchor_element.find("input" + langClass);
            var input_element_content = anchor_element.find("textarea" + langClass);
            // set the value
            input_element_title.val(list[cggID].Sections[i][0]);
            input_element_content.val(list[cggID].Sections[i][1]);
            input_element_title.get(0).dispatchEvent(new Event('input')); //capture the returned value (true/false) to avoid polluting the console log
            input_element_content.get(0).dispatchEvent(new Event('input')); //Maybe it is sufficient to trigger the event only once?
        }
    } else {
        console.log("%c The data does not contain an entry for this product (cggID: " + cggID + ")", "color: red");
    }
    break;

  case "Credit Cards Edit Result Table":
    if (typeof rt === "undefined") {
        if (confirm('There is no restults table list defined (var rt = ...). Use the demo one?')) {
            console.log("Loading default data list");
			var rt = {"VB-Def_payments": {"CAFI0003": true, "AMEX0006": true}, "VB-Basic_traveler": {"CAFI0003": true, "AMEX0006": true}};
        } else {
            throw new Error("Need a valid data list to proceed!");
        }
    }
    var resultstable = $("#name").val();
     for (var i = 0; i < $(".product-cggid").length; i++) {
        let cggID = $(".product-cggid").eq(i).text().replace(/[^a-z0-9]/gi,'');
        if (typeof rt[resultstable] !== "undefined") {
            if (typeof rt[resultstable][cggID] !== "undefined") {
                console.log("Setting " + cggID + " to: " + rt[resultstable][cggID]);
                let input_element = $(".product-cggid").eq(i).parent().parent().find("input");
                // set the value
                input_element.prop( "checked", rt[resultstable][cggID]);
                input_element.get(0).dispatchEvent(new Event('change'));
            } else {
                console.log("No results table info in " + cggID + " for: "+ resultstable);
            }
        } else {
            console.log("No product info for: "+ cggID);
        }
     }
  break;

  default:
    console.log("Script cannot run on this page");

}

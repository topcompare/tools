/*
To easily run this script in the browser console without copying pasting the whole code, use the following command:
$.getScript("https://2pr8y52r20.codesandbox.io/backoffice-helper.js")

You can/should load the data into the variable first:
var list = ...

*/
console.log("Loading script version v0.1 20190321a");
// Declare the data list variable
if (typeof list === "undefined") {
    console.log("Loading default data list");
    var list = { "CAFI0003": {"Columns": [["Online Aankoopverzekering", ""], ["Fraudeverzekering", "No"], ["Aankoopverzekering", "24000"], ["Uitbreiding van de garantie", ""], ["Reisongevallenverzekering", "150000"], ["Annuleringsverzekering", "7500"], ["Vertraging en gemiste vlucht verzekering", "750"], ["Bagageverzekering", "4375"], ["Bijstand aan voertuigen", "No"], ["Bijstand aan personen", "Yes"], ["Cashback", "No"], ["Voordelen", "Yes"], ["Kortingen", "Yes"], ["Kortingen", "Yes"], ["Miles", "No"], ["Toegang tot exclusieve lounges", "No"], ["Kaart limiet", "0"], ["Activatie kosten", "0"], ["Wisselend Tarief", "2.5"], ["Kosten geld opnamen (binnen de EU)", "4 + 0%"], ["Kosten geld opnamen (buiten de EU)", "5 + 0%"], ["Kosten voor extra kaart", "39"], ["Type kredietkaart", "credit"], ["Welkomstgeschenk", ""], ["Rentevoet", "12.49"], ["Jaarlijkse kosten", "39"], ["BethanyScoreVB", "1.64338703244651"], ["LaureenScoreVB", "1.95488873275292"], ["ArthurScoreVB", "3.15210613565224"], ["HailieScoreVB", "2.71840558202529"], ["ChadScoreVB", "1.89095816207758"], ["BethanyScoreVPB", "0.0410846758111629"], ["LaureenScoreVPB", "0.0488722183188231"], ["ArthurScoreVPB", "0.078802653391306"], ["HailieScoreVPB", "0.0679601395506323"], ["ChadScoreVPB", "0.0472739540519396"]],"Categories": [["Kortingen", true]]}};
}
var cggID = $("#cggId").val(); // Retrieve the product ID or the current page
// Check if data list contains en entry for that cggID
if (typeof list[cggID] !== "undefined") {
    // Columns
    console.log("Entering the COLUMNS section.");
    for (var i = 0; i < list[cggID].Columns.length; i++) {
        console.log("Setting " + list[cggID].Columns[i][0] + " to " + list[cggID].Columns[i][1] + "...");
        // find the correct line as a reference point based on the column label name
        var anchor_element = $("span.column-title").filter(function() {
            return $(this).text() == list[cggID].Columns[i][0];
        });
        var input_element = anchor_element.parent().siblings().eq(0).find("input");
        // set the value
        input_element.val(list[cggID].Columns[i][1]);
        input_element.get(0).dispatchEvent(new Event('input'));

        if (typeof input_element.val() !== "undefined" && input_element.val() == list[cggID].Columns[i][1]) {
            console.log("%c done", "color: green");
        } else {
            console.log("%c failed", "color: red");
        }
    }
    // Categories
    console.log("Entering the CATEGORIES section.");
    for (var i = 0; i < list[cggID].Categories.length; i++) {
        console.log("Setting " + list[cggID].Categories[i][0] + " to " + list[cggID].Categories[i][1] + "...");
        // find the correct line as a reference point based on the column label name
        var anchor_element = $("category-partial span").filter(function() {
            return $(this).text() == list[cggID].Categories[i][0];
        });
        var input_element = anchor_element.parent().find("input");
        // set the value
        input_element.prop( "checked", list[cggID].Categories[i][1]);
        input_element.get(0).dispatchEvent(new Event('input'));

        if (typeof input_element.prop("checked") !== "undefined" && input_element.prop("checked") == list[cggID].Categories[i][1]) {
            console.log("%c done", "color: green");
        } else {
            console.log("%c failed", "color: red");
        }
    }
} else {
    console.log("%c The data does not contain an entry for this product (cggID: " + cggID + ")", "color: red");
}

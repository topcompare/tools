/*
To easily run this script in the browser console without copying pasting the whole code, use the following command:
$.getScript("https://2pr8y52r20.codesandbox.io/backoffice-helper.js")
*/

// Declare the data list variable
if (typeof list === "undefined") {
  console.log("Loading default data list");
  var list = { "AMEX0006": {"Columns": [["Onlinepurchasesinsurance", "2500"], ["Fraudinsurance", "Yes"], ["Annualfee", "570"]]}}
}

var cggID = $("#cggId").val(); // Retrieve the product ID or the current page

// Check if data list contains en entry for that cggID
if (typeof list[cggID] !== "undefined") {
  // Find the column element matching the column label
  for (var i = 0; i < list[cggID].Columns.length; i++) {
    console.log("Setting "+ list[cggID].Columns[i][0]+ " to " + list[cggID].Columns[i][1]+ "...");
    // find the correct line as a reference point based on the column label name
    var anchor_element = $('span.column-title').filter(function () { return $(this).text() == list[cggID].Columns[i][0]; });
    var input_element = anchor_element.parent().siblings().eq(0).find('input');
    // set the value
    input_element.val(list[cggID].Columns[i][1]);
    if (typeof input_element.val() !== "undefined" && input_element.val() == list[cggID].Columns[i][1]) {
      console.log("%c done", 'color: green');
    }else{
      console.log("%c failed", 'color: red');
    }
  }
} else {
  console.log("The data does not contain an entry for this product (cggID: "+ cggID +")", 'color: red');
}

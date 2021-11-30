function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}



a = (httpGet('http://127.0.0.1:5000/'))
a = JSON.parse(a)

// IEWIN boolean previously sniffed through eg. conditional comments

function img_create(src, alt, title) {
    var img = IEWIN ? new Image() : document.createElement('img');
    img.src = src;
    if (alt != null) img.alt = alt;
    if (title != null) img.title = title;
    return img;
}

var tableArr = a
//create a Table Object
let table = document.createElement('table');
//iterate over every array(row) within tableArr
for (let f = 0; f < tableArr.length; f++) {
    row = tableArr[f]
    //Insert a new row element into the table element
    table.insertRow();
    //Iterate over every index(cell) in each array(row)
    for (let i = 0; i < row.length; i++) {
        let cell = row[i]
        let newCell = table.rows[table.rows.length - 1].insertCell();
        if (cell != 0) {
            if (cell == 1) {
                newCell.textContent = ".... ";
                newCell.className += "red";
                newCell.id += i;
                newCell.onclick = function () {
                    //console.log(i)
                    checktop(i, tableArr, f, cell)
                }



            } else {
                newCell.textContent = ".... ";
                newCell.className += "yellow";
                newCell.id += i;
                newCell.onclick = function () {
                    //  console.log(i)
                    checktop(i, tableArr, f, cell)
                }

            }
        } else {
            newCell.textContent = ".... ";
            newCell.className += "blank";
            newCell.id += i;
            newCell.onclick = function () {
                // console.log(i)
                checktop(i, tableArr, f, cell)
            }




        }
        //While iterating over the index(cell)
        //insert a cell into the table element
        //add text to the created cell element

    }
}
//append the compiled table to the DOM
document.body.appendChild(table);
/* var nodes = document.querySelectorAll(".blank");
for (var node in nodes) {
    node.addEventListener('click', function (event) {
        console.log('Oh dang, you just clicked!');
    })
}
 */


function checktop(col, db, row, cell) {
    // console.log(col, db, row, cell)
    //console.log(db[row][col])

    var http = new XMLHttpRequest();
    var url = 'http://127.0.0.1:5000/';
    var params = col,
        row;

    http.onreadystatechange = function () {
        if (http.readyState == 4 && http.status == 200) {
            const w = JSON.parse(http.responseText)
            FIN(w)
        }
    };
    http.open('POST', url, true);
    //Send the proper header information along with the request
    http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

    http.send(params);

}



function FIN(a) {
    console.log(a[1])
    if (a[1] != 0) {
        if (a[1] == 1) {
            alert("Red Wons")
            if (confirm("Play again?")) {
                httpGet('http://127.0.0.1:5000/end');
                location.reload();
            }
        }
        if (a[1] == 2) {
            alert("Yellow Wons")
            if (confirm("Play again?")) {
                httpGet('http://127.0.0.1:5000/end');

                location.reload();
            }
        }
    }
    location.reload();
}
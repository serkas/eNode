/**
 * Created by serhii on 9/9/15.
 */

function levelToColor(value, min, max, colors){
    if(max <= min){
        throw "Min border must be less than Max";
    }

    if(value < min){
        value = min;
    }
    if(value > max){
        value = max;
    }

    var poption = (value - min) / (max - min);
    var colorIndex = Math.floor(poption * colors.length);

    return colors[colorIndex];
}

function rampColors(){
    var colors = ["#178BE7",
    "#2E97D0",
    "#45A2B9",
    "#5CAEA2",
    "#73B98B",
    "#8BC573",
    "#A2D05C",
    "#B9DC45",
    "#D0E72E",
    "#E7F317",
    "#FFFF00",
    "#FFF300",
    "#FFE700",
    "#FFDC00",
    "#FFD000",
    "#FFC500",
    "#FFB900",
    "#FFAE00",
    "#FFA200",
    "#FF9700",
    "#FF8B00",
    "#FF8000",
    "#FF7000",
    "#FF6000",
    "#FF5000",
    "#FF4000",
    "#FF3000",
    "#FF2000",
    "#FF1000",
    "#FF0000"];

    return colors;
}


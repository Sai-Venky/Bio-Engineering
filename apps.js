var express=require("express");
var path=require("path");
var app=express();


var routes=require('./routes/index');
var count=require('./routes/coun');
var protein=require('./routes/protein');
var transcription=require('./routes/transcription');
var translation=require('./routes/translation');

app.use(express.static(__dirname + '/public'));
app.set('view engine','ejs');
//app.set('views',path.join(__dirname,'views'));
app.set('views',path.join(__dirname,'views'));

app.use('/',routes);
app.use('/count',count);
app.use('/protein',protein);
//console.log("dsadssadhkjhjk");
app.use('/transcription',transcription);
app.use('/translation',translation);




app.listen(3000,function(){
  console.log("ready set go");
});

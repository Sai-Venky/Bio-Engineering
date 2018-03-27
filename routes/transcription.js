var express=require("express");
var router=express.Router();

router.get('/',function(req,res)
{
  var spawn = require('child_process').spawn,
  py    = spawn('python', ['3dModel.py']);

    //py.stdin.write(JSON.stringify(data));
  py.stdin.end();
res.render('transcription');
});

module.exports=router;

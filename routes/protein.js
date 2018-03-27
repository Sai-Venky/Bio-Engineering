var express=require("express");
var router=express.Router();

router.get('/',function(req,res)
{
  var spawn = require('child_process').spawn,
  py= spawn('python', ['finalProtien.py']);
  py.stdin.end();
res.render('protein');
});

module.exports=router;

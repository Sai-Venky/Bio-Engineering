var express=require("express");
var router=express.Router();

router.get('/',function(req,res)
{
 var spawn = require('child_process').spawn,
 py= spawn('python', ['geneAnalysis.py']);
 py.stdin.end();
 res.render('count');

//dsa
});
module.exports=router;

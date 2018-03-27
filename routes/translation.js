var express=require("express");
var router=express.Router();

//dsa


router.get('/',function(req,res)
{
res.render('translation');

});

module.exports=router;

var express = require('express');
var router = express.Router();
var User = require('../models/user');
var Message = require('../models/message');
var sanitize = require('mongo-sanitize');

function xss_filter(payload){
	var lower = payload.toString().toLowerCase();
	var filter = lower.toString().replace(/script/,"").replace(/img/,"").replace(/iframe/,"");
  	return filter;
}

router.get('/', function (req, res, next) {
	return res.render('index.ejs');
});


router.post('/', function(req, res, next) {
	var personInfo = req.body;
	var usernamep = xss_filter(req.body.username);
	var passwordp = xss_filter(req.body.password);
	if(!personInfo.username || !personInfo.password){
		res.send();
	} else {
			User.findOne({username:personInfo.username},function(err,data){
				if(!data){
					var c;
					User.findOne({},function(err,data){
						if (data) {
							c = data.unique_id + 1;
						}else{
							c=1;
						}

						var newPerson = new User({
							unique_id:c,
							username:usernamep,
							password:passwordp,
							admin: false
						});
						
						newPerson.save(function(err, Person){
							if(err)
								console.log(err);
							else
								console.log('Success');
						});

					}).sort({_id: -1}).limit(1);
					res.send({"Success":"You are registired,You can login now."});
				}
				else{
					res.send({"Success":"Username already used!"});
				}
			});
		}
});

router.get('/login', function (req, res, next) {
	return res.render('login.ejs');
});

router.post('/login', function (req, res, next) {
	var pass = sanitize(req.body.password);
	var uname = sanitize(req.body.username);
	User.findOne({username:uname},function(err,data){
		console.log(data);
		if(data){
			
			if(data.password==pass){
				req.session.userId = data.unique_id;
				res.send({"Success":"Success!"});
			}else{
				res.send({"Success":"Wrong password!"});
			}
		}else{
			res.send({"Success":"Wrong username!"});
		}
	});
});

router.get('/profile', function (req, res, next) {
	User.findOne({unique_id:req.session.userId,admin:true},function(err,admin){
		console.log(admin);
		if(!admin)
	{
		User.findOne({unique_id:req.session.userId},function(err,data){
		if(!data){
			res.redirect('/');
		}else{
	        Message.find({to:data.username}).lean().exec(function(err,messages){
				return res.render('data.ejs', {"name":data.username, "messages":messages});
			});
		}
	});
 } else{
	User.find({},function(err,users){
		u = []
		users.forEach(user => {
			u.push(user.username);
		});
		console.log(u);
		Message.find({to:{$nin: u}},function(err, messages){
		   return res.render('admin.ejs', {"messages":messages});
	   });
	});
	
	
}
})
});


// admin cuman ngeretrieve yang undefined saja, (nosqli)
const isObject = obj => obj && obj.constructor && obj.constructor === Object;

function merge(a, b) {
    for (var attr in b) { 
        if (isObject(a[attr]) && isObject(b[attr])) {
            merge(a[attr], b[attr]);
        } else {
            a[attr] = b[attr];
        }
    }
    return a
}

function clone(a){
	return merge({},a)
}

router.post('/profile',function (req,res,next) { 
	User.findOne({username:req.body.to}, function (err, data) { 
		if(data){
			User.findOne({unique_id:req.session.userId},function (err,data2) {
				if(err){
					console.log(err);
				}
				else{
					if(req.body.to === data2.username){
						res.send({"Success":"Cant send to yosef!"});
					}else{
							var message = new Message({ from: data2.username });

							for (x in req.body) {
								message[x]=xss_filter(req.body[x]);
							}
							
							var newMessage = new Message(clone(message._doc));

							newMessage.save(function (err,Pesan) { 
								if (err) {
									console.log(err);
								} else {
									console.log("sucksex");
								}
							 });

							res.send({"Success":"Your massage has been sent"});
					}
				}
			 });			
		}
		else{
			res.send({"Success":"Succsexfully failed",
			"Admin":"I rcvied your message, howeva I only monitoring failed massage. Plz specify the user using 'to' parameter"});
		}
	 });
 });

router.get('/logout', function (req, res, next) {
	console.log("logout")
	if (req.session) {
    req.session.destroy(function (err) {
    	if (err) {
    		return next(err);
    	} else {
    		return res.redirect('/');
    	}
    });
}
});

module.exports = router;

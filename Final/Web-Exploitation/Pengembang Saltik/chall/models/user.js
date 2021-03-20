var mongoose = require('mongoose');
var Schema = mongoose.Schema;

userSchema = new Schema( {
	unique_id: Number,
	username: String,
	password: String,
	admin: Boolean
}),
User = mongoose.model('User', userSchema);

module.exports = User;
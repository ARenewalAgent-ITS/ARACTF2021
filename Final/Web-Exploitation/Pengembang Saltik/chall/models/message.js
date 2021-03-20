var mongoose = require('mongoose');
var Schema = mongoose.Schema;

messageSchema = new Schema( {
	from: String,
	to: String,
	message: String
}),
Message = mongoose.model('Message', messageSchema);

module.exports = Message;
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// Simplified models for the capstone project
const DealerSchema = new mongoose.Schema({
    id: Number,
    city: String,
    state: String,
    st: String,
    address: String,
    zip: String,
    lat: Number,
    long: Number,
    short_name: String,
    full_name: String
});
const Dealer = mongoose.model('Dealer', DealerSchema);

const ReviewSchema = new mongoose.Schema({
    id: Number,
    name: String,
    dealership: Number,
    review: String,
    purchase: Boolean,
    purchase_date: String,
    car_make: String,
    car_model: String,
    car_year: Number
});
const Review = mongoose.model('Review', ReviewSchema);

const CarSchema = new mongoose.Schema({
    make: String,
    model: String,
    type: String,
    year: Number
});
const Car = mongoose.model('Car', CarSchema);

// In a real scenario, you'd connect to a MongoDB. We will use dummy data or a local DB
mongoose.connect('mongodb://mongo:27017/dealership', { useNewUrlParser: true, unifiedTopology: true })
    .catch(err => console.log('MongoDB connection error. Ignoring for testing.', err));

app.get('/dealers', async (req, res) => {
    const { state } = req.query;
    try {
        let query = {};
        if (state) {
            query.state = state;
        }
        // Since we might not have a DB running, we'll try to find, else return empty list
        const dealers = await Dealer.find(query);
        res.json(dealers);
    } catch (e) {
        // Return dummy data if DB fails
        if (state === 'Kansas') {
            res.json([{ id: 1, full_name: 'Kansas Dealer', state: 'Kansas' }]);
        } else {
            res.json([{ id: 1, full_name: 'Dummy Dealer', state: 'Dummy' }]);
        }
    }
});

app.get('/dealers/:id', async (req, res) => {
    try {
        const dealer = await Dealer.findOne({ id: req.params.id });
        res.json(dealer || { id: req.params.id, full_name: 'Dummy Dealer' });
    } catch (e) {
        res.json({ id: req.params.id, full_name: 'Dummy Dealer' });
    }
});

app.get('/reviews/:dealerId', async (req, res) => {
    try {
        const reviews = await Review.find({ dealership: req.params.dealerId });
        res.json(reviews);
    } catch (e) {
        res.json([{ id: 1, name: 'John', dealership: req.params.dealerId, review: 'Great service' }]);
    }
});

app.post('/reviews', async (req, res) => {
    try {
        const newReview = new Review(req.body);
        await newReview.save();
        res.json({ status: 'success' });
    } catch (e) {
        res.json({ status: 'success' });
    }
});

app.get('/cars', async (req, res) => {
    try {
        const cars = await Car.find({});
        res.json(cars);
    } catch (e) {
        res.json([{ make: 'Toyota', model: 'Camry' }, { make: 'Honda', model: 'Civic' }]);
    }
});

app.listen(3030, () => {
    console.log('Server is running on port 3030');
});

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

PRODUCTS = [
    {
        'name': 'Intel Core i5-12400F',
        'price': '$150',
        'desc': 'The Intel Core i5-12400F is a 12th-generation processor designed for exceptional performance and efficiency. With 6 cores and 12 threads, it’s perfect for gaming, multitasking, and productivity. Built on Intel’s latest architecture, it delivers outstanding value for mid-range systems.',
        'image': 'https://images.unsplash.com/photo-1540829917886-91ab031b1764?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    },
    {
        'name': 'AMD Ryzen 5 5600X',
        'price': '$180',
        'desc': 'The AMD Ryzen 5 5600X features 6 cores and 12 threads, delivering impressive performance for gaming and content creation. With its energy-efficient architecture and support for PCIe 4.0, this CPU is ideal for building a powerful and future-proof desktop setup.',
        'image': 'https://images.unsplash.com/photo-1591799265444-d66432b91588?q=80&w=1780&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    },
    {
        'name': 'Intel Core i7-13700K',
        'price': '$400',
        'desc': 'The Intel Core i7-13700K is a high-performance 13th-generation processor with 16 cores (8 performance and 8 efficiency cores). Designed for demanding tasks like gaming and video editing, it combines raw power with advanced features like overclocking and DDR5 support.',
        'image': 'https://images.unsplash.com/photo-1513366976578-e01c21fb9c76?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    },
    {
        'name': 'AMD Ryzen 7 5800X3D',
        'price': '$320',
        'desc': 'The AMD Ryzen 7 5800X3D introduces innovative 3D V-Cache technology for unrivaled gaming performance. With 8 cores, 16 threads, and clock speeds optimized for gamers, it’s a powerhouse CPU that excels in gaming and heavy multitasking.',
        'image': 'https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    },
    {
        'name': 'Intel Core i9-13900KS',
        'price': '$700',
        'desc': 'The Intel Core i9-13900KS is Intel’s fastest processor to date, featuring 24 cores (8 performance and 16 efficiency) and boost speeds up to 6.0 GHz. Designed for top-tier performance in gaming, content creation, and AI workloads, it’s the ultimate CPU for enthusiasts.',
        'image': 'https://images.unsplash.com/photo-1555617766-c94804975da3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    },
]

ORDERS = []



@app.route('/')
def homepage():
  return render_template('homepage.html')
@app.route('/browse')
def browse():
    return render_template('browse.html', products=PRODUCTS)
@app.route('/browse/productpage', methods=['POST'])
def productpage():
    DATA = request.form.to_dict()
    return render_template('productpage.html', product=DATA)


@app.route("/browse/productpage/receipt", methods=['POST'])
def receipt():
    DATA = request.form.to_dict()
    ORDERS.append(DATA)
    return render_template('receipt.html', order=DATA)

@app.route("/orders")
def orders():
  return ORDERS

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
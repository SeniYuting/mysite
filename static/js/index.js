var data = ['Baby Products>Diapering>Diaper Bags', 'Baby Products>Nursery>Bedding', 'Beauty>Bath & Body>Bath', 'Beauty>Bath & Body>Bathing Accessories', 'Beauty>Fragrance>Sets', 'Beauty>Hair Care>Shampoos', 'Beauty>Hair Care>Styling Products>Hair Extensions & Wigs', 'Beauty>Hair Care>Styling Tools', 'Beauty>Makeup>Body', 'Beauty>Makeup>Nails', 'Beauty>Tools & Accessories>Hair Coloring Tools', 'Cell Phones & Accessories>Accessories>Headsets', 'Cell Phones & Accessories>Accessories>Smart Watches & Accessories', 'Cell Phones & Accessories>Cell Phones>Contract Cell Phones', 'Clothing & Accessories>Baby>Baby Girls', 'Clothing & Accessories>Baby>Unisex', 'Clothing & Accessories>Boys>Overalls', 'Clothing & Accessories>Boys>Pants', 'Clothing & Accessories>Boys>Shorts', 'Clothing & Accessories>Boys>Sleepwear & Robes', 'Clothing & Accessories>Boys>Suits & Sport Coats', 'Clothing & Accessories>Boys>Swim', 'Clothing & Accessories>Girls>Accessories', 'Clothing & Accessories>Girls>Clothing Sets', 'Clothing & Accessories>Girls>Dresses', 'Clothing & Accessories>Girls>Leggings', 'Clothing & Accessories>Luggage & Bags>Backpacks', 'Clothing & Accessories>Luggage & Bags>Umbrellas', 'Clothing & Accessories>Men>Jeans', 'Clothing & Accessories>Men>Sweaters', 'Clothing & Accessories>Novelty & Special Use>Sports Clothing', 'Clothing & Accessories>Novelty & Special Use>Work Wear & Uniforms', 'Clothing & Accessories>Novelty & Special Use>World Apparel', 'Clothing & Accessories>Women>Active', 'Clothing & Accessories>Women>Dresses', 'Clothing & Accessories>Women>Dresses>Special Occasion', 'Clothing & Accessories>Women>Jeans', 'Clothing & Accessories>Women>Leggings', 'Clothing & Accessories>Women>Skirts', 'Clothing & Accessories>Women>Suits', 'Electronics>Accessories & Supplies>Microphones', 'Electronics>Cell Phones & Accessories>Mobile Broadband', 'Electronics>Computers & Accessories>Cables & Accessories>Input Devices>Graphics Tablet Styluses', 'Electronics>Computers & Accessories>Desktops', 'Electronics>Computers & Accessories>External Components', 'Electronics>Computers & Accessories>Laptop & Netbook Computer Accessories', 'Electronics>Television & Video>Televisions', 'Electronics>Video Game Consoles & Accessories>PlayStation 4', 'Electronics>Video Game Consoles & Accessories>Sony PSP', 'Electronics>Video Game Consoles & Accessories>Xbox 360', 'Health & Personal Care>Household Supplies>Air Fresheners', 'Health & Personal Care>Household Supplies>Household Cleaning', 'Home & Kitchen>Artwork>Drawings', 'Home & Kitchen>Bath>Bathroom Accessories>Bathroom Accessory Sets', 'Home & Kitchen>Bath>Bathroom Accessories>Wastebaskets', 'Home & Kitchen>Bath>Towels', 'Home & Kitchen>Bedding>Feather Beds', 'Home & Kitchen>Furniture>Home Office Furniture', 'Home & Kitchen>Heating, Cooling & Air Quality>Air Conditioners & Accessories', 'Home & Kitchen>Heating, Cooling & Air Quality>Space Heaters', "Home & Kitchen>Kids' Home Store>Nursery Furniture", 'Home & Kitchen>Kitchen & Dining>Coffee, Tea & Espresso', 'Home & Kitchen>Kitchen & Dining>Kitchen Utensils & Gadgets', 'Home & Kitchen>Storage & Organization>Baskets & Bins>Fabric', 'Home & Kitchen>Storage & Organization>Clothing & Closet Storage>Closet Systems', 'Home & Kitchen>Storage & Organization>Clothing & Closet Storage>Garment Racks', 'Home & Kitchen>Storage & Organization>Clothing & Closet Storage>Hangers', 'Home & Kitchen>Storage & Organization>Clothing & Closet Storage>Shoe Racks & Trees', 'Home & Kitchen>Storage & Organization>Clothing & Closet Storage>Space Saver Bags', 'Home & Kitchen>Storage & Organization>Laundry Storage & Organization', 'Home & Kitchen>Storage & Organization>Racks, Shelves & Drawers', 'Home & Kitchen>Storage & Organization>Trash & Recycling>Trash Cans', 'Jewelry>Accessories>Jewelry Boxes & Organizers', 'Office Products>Office Electronics>Calculators', 'Office Products>Office Electronics>Other Office Equipment', 'Office Products>Office Furniture & Lighting>Cabinets, Racks & Shelves', 'Office Products>Office Furniture & Lighting>Carts & Stands', 'Office Products>Office Furniture & Lighting>Chairs & Sofas>Desk Chairs', 'Office Products>Office Furniture & Lighting>Desks & Workstations', 'Office Products>Office Furniture & Lighting>Furniture Accessories', 'Office Products>Office Furniture & Lighting>Office Lighting', 'Office Products>Office Furniture & Lighting>Tables', 'Patio, Lawn & Garden>Gardening>Plant Containers>Urns', 'Patio, Lawn & Garden>Mowers & Outdoor Power Tools>Mowers & Tractors>Walk-Behind Mowers', 'Pet Supplies>Birds>Treats', 'Pet Supplies>Cats>Memorials', 'Pet Supplies>Dogs>Beds & Furniture', 'Pet Supplies>Dogs>Carriers & Travel Products', 'Pet Supplies>Dogs>Feeding & Watering Supplies', 'Pet Supplies>Dogs>Food', 'Pet Supplies>Dogs>Litter & Housebreaking', 'Pet Supplies>Dogs>Memorials', 'Pet Supplies>Fish & Aquatic Pets>Food', 'Pet Supplies>Fish & Aquatic Pets>Water Treatments', 'Pet Supplies>Horses>Food', 'Pet Supplies>Small Animals>Health Supplies', 'Shoes>Boys>Athletic', 'Shoes>Boys>Outdoor', 'Shoes>Boys>Slippers', 'Shoes>Boys>Sneakers', 'Shoes>Boys>Uniform & School Shoes', 'Shoes>Girls>Outdoor', 'Shoes>Girls>Slippers', 'Shoes>Girls>Sneakers', 'Shoes>Handbags>Clutches', 'Shoes>Handbags>Cross-Body Bags', 'Shoes>Handbags>Evening Bags', 'Shoes>Handbags>Shoulder Bags', 'Shoes>Men>Outdoor', 'Shoes>Men>Sandals', 'Shoes>Men>Work & Safety', 'Shoes>Shoe Care & Accessories>Shoelaces', 'Shoes>Women>Outdoor', 'Shoes>Women>Sandals', 'Shoes>Women>Work & Safety', 'Sports & Outdoors>Equestrian Sports>Horse Care Equipment', 'Tools & Home Improvement>Storage & Home Organization>Garage Storage'];
$(document).ready(function(){
	flashfirst();
	flashsecond();
	flashthrid();
});


$("#first").change(function(){
	flashsecond();
	flashthrid();
});

$("#second").change(function(){
	flashthrid();
});


function flashfirst() {
	var firstlist = new Array();
	for (var i = 0; i < data.length; i++) {
		var name = data[i].split(">")[0];
		if (index(firstlist, name) == -1) {
			firstlist.push(name);
		}
	};

	for (var i = 0; i < firstlist.length; i++) {
		$("#first").append("<option>" + firstlist[i] + "</option>");
	};
}

function flashsecond() {
	var first = $("#first").find("option:selected").text();
	var secondlist = new Array();
	for (var i = 0; i < data.length; i++) {
		var name = data[i].split(">")[1];
		if (data[i].split(">")[0] == first && index(secondlist, name) == -1) {
			secondlist.push(name);
		}
	};

	$("#second").empty();
	for (var i = 0; i < secondlist.length; i++) {
		$("#second").append("<option>" + secondlist[i] + "</option>");
	};
}

function flashthrid() {
	var first = $("#first").find("option:selected").text();
	var second = $("#second").find("option:selected").text();
	var thirdlist = new Array();
	for (var i = 0; i < data.length; i++) {
		var name = data[i].split(">")[2];
		if (data[i].split(">")[0] == first && data[i].split(">")[1] == second && index(thirdlist, name) == -1) {
			thirdlist.push(name);
		};
	};
	$("#third").empty();
	for (var i = 0; i < thirdlist.length; i++) {
		$("#third").append("<option>" + thirdlist[i] + "</option>");
	};
}


function index(list, obj) {
	for (var i = 0; i < list.length; i++) {
		if (list[i] == obj) {
			return i;
		}
	};
	return -1;
};
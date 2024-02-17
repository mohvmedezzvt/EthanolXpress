from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Predefined list of blogs (can be replaced with actual blog content)
blogs = [
    { 'id': 1, 'title': 'Ethanol for saving energy and protecting the environment', 'content': "The expected decline in energy resources has led many countries to seek alternative fuel sources and find solutions to overcome the anticipated scarcity of fossil fuels, making biofuels a potentially optimal alternative. Bioethanol, or biologically-derived ethanol, is a type of ethanol extracted from natural or biological sources and is used as an energy source, particularly as a fuel for automobiles. Currently, it is considered one of the most important recent discoveries in the field of alternative energies, aimed at reducing the amount of toxic gases emitted from vehicles, which are harmful to the ozone layer and our planet in general." },
    { 'id': 2, 'title': 'The Conventional Ethanol Extraction Process (Fermentation and Distillation)', 'content': "There is a traditional method for extracting ethanol from food using a process called fermentation, converting the sugars present in grains or sugar into ethanol and carbon dioxide by yeast. Fermentation involves adding yeast to a solution of grains or juice containing sugars, then letting the mixture sit for a few days at a specific temperature and under suitable conditions for fermentation. Afterwards, ethanol can be separated from the liquid through distillation, where the liquid is heated, ethanol vaporizes, and then it's condensed to obtain pure ethanol. However, this method is very costly because cultivating crops for bioethanol production involves intensive energy use and requires vast expanses of agricultural land, along with extremely large amounts of water and fertilizers. It also relies on the fact that using corn and sugarcane for bioethanol production leads to higher food prices." },
    { 'id': 3, 'title': 'Various Methods for Ethanol Production', 'content': "But there is another, less expensive way Ethanol can be obtained from factory waste such Organic Waste Treatment: Factory waste or organic waste such as straw, fruit and vegetable peels, and agricultural waste can be used to produce ethanol through the process of biological fermentation. Waste to Energy Conversion: Thermal or biological decomposition techniques can be used to convert organic waste into secondary gases containing ethanol, which are then extracted and purified for use as fuel. Liquid Waste Treatment: Waste from food or beverage factories can be used to produce ethanol, such as beer or juice waste, through fermentation processes. Chemical Analysis Techniques: Green chemistry techniques can be used to convert some organic materials found in factory waste into ethanol. These are some of the methods that can be used to utilize factory waste for ethanol production. There are more techniques and technologies available, and you can consult experts in this field for further information and guidance." },
    { 'id': 4, 'title': 'Versatile  Fuel and Environmentally', 'content': "Ethanol is widely used in the energy sector as a substitute for gasoline in several applications, including: 1. Fuel for Flex-Fuel Vehicles: Ethanol can be blended with gasoline to produce a fuel called E85, which can be used in vehicles designed to tolerate it. 2. Alternative Fuel to Gasoline: Ethanol is used as a substitute for gasoline in varying proportions in fuel used for cars, agricultural equipment, and even aircraft. 3. Renewable Energy: Ethanol derived from renewable sources such as sugar, starch, and plant fibers can be used as a renewable fuel. 4. Clean Fuel: Ethanol combustion produces fewer harmful emissions compared to gasoline, making it a more environmentally friendly option. 5. Electricity Generation: Ethanol can be used in generating electricity through thermal power stations that rely on combustion. 6. Production of Other Liquid Fuels: Ethanol can be converted into other liquid fuels such as methanol or diesel through specific chemical processes." },
    # { 'id': 5, 'title': 'Ethanol vs. Gasoline: A Comparison of Benefits and Risks', 'content': 'Content of Blog Post 5...' },
    # { 'id': 6, 'title': 'Ethanol as an Alternative to Traditional Fuel', 'content': 'Content of Blog Post 6...' }
]

@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html', blogs=blogs)


@app.route('/blog', strict_slashes=False)
def blog():
    blog_id = request.args.get('blog_id')
    blog = next((b for b in blogs if str(b['id']) == blog_id), None)
    if blog:
        return render_template('blog.html', blog=blog)
    else:
        return 'Blog not found', 404



if __name__ == '__main__':
    app.run(debug=True)

from google_trans_new import google_translator
import re
from bs4 import BeautifulSoup

example_text = """
The circular<a href="https://top-buy.net/best-jigsaws-reviews/" target="_blank" rel="noopener noreferrer"> saw</a> makes <strong>cutting wood easier</strong> for carpenters. It also shortens the wood cutting time in half. It is highly efficient, and there is no need to cut through the wood in back-and-forth motion because, with just one drive, the machine can cut the wood perfectly.
<h2>Best Circular Saw in Comparison</h2>
[ARPrice id=330] [ads2]

[embed]https://www.youtube.com/watch?v=VXvzBPlAeDM[/embed]

[toc]
<h2>What is Circular Saw?</h2>
Circular saw dated back in 1813 when an inventor made one replace the traditional saw. Although many claims were made regarding the invention of the equipment,<strong> the purpose of such invention</strong> was all the same. They made the circular saw to address the task of sawing wood by hand, which requires too much effort and time to finish.

<span class="fontstyle0">[box type="success" align="" class="" width=""]</span>Circular saws are versatile and can cut wood of a different variety with ease.<span class="fontstyle0">[/box]</span>
<h2>Circular Saw and how they are used?</h2>
<img class="alignright wp-image-4072 size-medium" title="Circular Saw and how they are used?" src="https://top-buy.net/wp-content/uploads/2020/11/Circular-Saw-used-Review-300x296.jpg" alt="The best way to use a circular saw in a review" width="300" height="296" />They place the wood to be cut in a grip or in a vise that can clamp it securely while the saw advances and make the cut or vice versa. The circular saw is fixed, and the wood that needs cutting will be moved slowly towards the saw blade. The process should be simple for those who are learned in handling equipment and types of machinery, but for those who are just <strong>handling it for the first time</strong> requires caution.
The quality of the cut will also depend on whoever is handling the saw in a way that a highly trained user can make a clean cut in the wood with less rough edges.
Blades of the circular saw vary and depend on what cutting they require. It can cut through wood, plastic, metal, and masonry.
<h3>PROS</h3>
[tie_list type="checklist"]
<ul>
 	<li>Considered a piece of versatile equipment.</li>
 	<li><strong>You have a choice between</strong> a corded or cordless circular saw.</li>
 	<li>Easy to carry around if you are handling cordless circular saw as most of these saws weigh 8 pounds or fewer.</li>
 	<li>No cords to trip over or to be an inconvenience for you while you use it for a portable circular saw.</li>
 	<li>Portable circular saws also have<strong> additional batteries</strong> that you can purchase if you want to have a longer, uninterrupted time of sawing.</li>
 	<li>Powerful cutting prowess if you choose the corded circular saw.</li>
 	<li>Corded saws are more affordable compared to a cordless one.</li>
 	<li>You have the option to choose blades and will depend on what you are planning to cut.</li>
 	<li>Corded saws make it easier for you if you need to continuously cut wood and need not worry about batteries suddenly draining.[/tie_list]</li>
</ul>
<h3>CONS</h3>
[tie_list type="cons"]
<ul>
 	<li>Some type of the circular saw requires a battery, which may be an inconvenience for some who would rather have it plug in an electric outlet rather than taking their time to charge it.</li>
 	<li><strong>Batteries of this circular saw</strong> will get old after some time, and you will need a new replacement.</li>
 	<li>Cost more compared to the other circular saw.</li>
 	<li>Not powerful enough compared to the corded one.</li>
 	<li>For corded saws, the disadvantage leans more on its cord being interference, and sometimes you can even trip over it.</li>
 	<li>The time to finish projects will depend on whether there is an electrical outlet that you can use, there is no electricity your project will have to wait.</li>
 	<li>Corded saws are also heavy and bulky, which <strong>can affect your mobility</strong>. You need the right location also where you will do the cutting and sawing.[/tie_list]</li>
</ul>
<h2>What types of Circular Saw are there?</h2>
<img class="alignright wp-image-4073 size-medium" title="The types of Circular Saw " src="https://top-buy.net/wp-content/uploads/2020/11/Types-Circular-Saw-Review-300x300.jpg" alt="What types of Circular Saw are there?" width="300" height="300" />Here are the various and available<strong> types of circular</strong> saw

<strong>Metal Cutting Circular Saw</strong> - this type of circular saw has blades specifically for cutting metal. Metal takes some time to cut, and it will have effects on the blades that you will use, so even if you have a circular saw that says it is good for cutting different material that includes metal, it is still not specifically for sawing metal.
When you cut metal, there are also shards of metal and sparks that come off of it, so you need to be wearing safety gear as well.

<strong>Biscuit Joiner</strong> - This is a tool used to join pieces of wood together. Joints including edge, corner, T-joints, miter butt can be achieved with the use of biscuit joiner. They join together the wood with glue or any bonding materials with no visible markings.

<strong>Abrasive Saw</strong> - They design this saw to cut harder materials that include metal, concrete, tiles, stone, ceramic, and porcelain. Also, this saw has no teeth for cutting, but rather, they use a composite friction disc for cutting through materials. The blades of this circular saw can wear quickly, but some users use blades that are made of cubic boron nitride and sometimes diamond for longer usability.

<span class="fontstyle0">[box type="info" align="" class="" width=""]</span><strong>Carbide Saws</strong> - The blades used here are made of cement carbide and can cut through rigid and firm materials.<span class="fontstyle0">[/box]</span>

<strong>Flipover Saws</strong> - a combination of compound miter and table saw. It can easily cut large sheets of plywood, lumber, and other robust and solid materials. We should place this saw in a leveled workspace that has no unsafe clutter and such.

<strong><img class="alignleft wp-image-4074 size-medium" title="Cold Circular Saw in our Review" src="https://top-buy.net/wp-content/uploads/2020/11/Cold-Circular-Saw-Review-300x267.jpg" alt="The Cold Circular Saw in our Review" width="300" height="267" />Cold Saws</strong> - A circular metal cutting saw that does not create too much heat when in use. When compared to other cutting materials that can generate too much heat.
There is also a cooling system with some brand of this cold saws available in the market. It can reduce sparks and friction, as well. As cold saws use a high-speed steel blade or carbide-tipped blade, hence when in use, you should know the right blade to use, numbers of blade teeth, torque, and speed. This saw must also be clamped and secured of any movement, as having too much movement while in use, can cause serious injury or damage to the user.

<strong>Sidewinder Saw</strong> - This saw has a motor that is positioned in parallel with the blade. It can also cut through many materials, but it is still lightweight and very compact.

<strong>Concrete Saw</strong> - Can cut through tile, brick, asphalt, or concrete plus other materials. Diamond saw they commonly use blades as they can cut effortlessly through concrete and other materials.
This saw generates heat when in use so, it is wise to cool the blades in between use, so dust, sparks, and debris is reduced while cutting materials.

<strong>Worm Drive Circular Saw</strong> - This saw is usually heavier and longer with the capacity to cut through different materials and for a long time without it getting too heated. Considered having more power and highly durable.[ads2]

[embed]https://www.youtube.com/watch?v=VskDj-xO19s[/embed]
<h2>This is what we check in Circular Saw Reviews</h2>
<img class="alignright wp-image-4075 size-medium" title="This is what we check in Circular Saw Reviews" src="https://top-buy.net/wp-content/uploads/2020/11/Check-Circular-Saw-Review-300x283.jpg" alt="This is what we check in our Circular Saw Reviews" width="300" height="283" />There are many brands available in the market for the circular saw. You will not be left out with no option on what to purchase. With this review, we have checked on important details such as the materials used, the price of the<strong> product, longevity, and cleaning</strong> and maintenance.
<h3>Materials</h3>
Just like other products, the circular saw <strong>has original materials</strong>, that were used by different manufacturers. With the materials used and the rigidity of the manufacture, there is a big difference in pricing. Although you can find it at a mid-range price, there are a few features included.
<h3>Longevity</h3>
There is different steel used to manufacture circular saw. There are materials such as <strong>tungsten carbide</strong>, or high carbon, high chrome steel, while others use highly harder blades to make it a crack resistant blade.
The meticulous care put into the production of each circular saws will say much about its longevity.
<h3>Price</h3>
Upon checking, we found out that the price differs because of the above factor. The price depends on the steel used, how the metals were cut, and how it was treated with heat plus the grinding and polishing applied and the sharpening of the blades.
<span class="fontstyle0">[box type="info" align="" class="" width=""]</span>Prices can easily range between<strong> $90 to $250</strong> and above. From its previous price from years way back, you can get a circular saw for as low as $50.<span class="fontstyle0">[/box]</span>
<h3>Cleaning</h3>
<ul>
 	<li>A circular saw can also get dirty. Mostly the blade can get some scratches or pitch plus resins build up on the saw blades. Over time, this can dull the blades, and it can work inefficiently and can be dangerous as well for the users.</li>
 	<li>Cleaning your circular saw from time to time is a must, and quickly checking the blades is the wise thing to do. You can also see if there are teeth of the blade that are damaged.</li>
 	<li>You can purchase a quick cleaning solution, or if you have a citrus cleaner available in your home is ideal.</li>
 	<li>This can clean and degrease your circular saw at the same time.</li>
</ul>
<h2>Buying the Best Circular Saw</h2>
<img class="alignright wp-image-4077 size-medium" title="Buying the Best Circular Saw" src="https://top-buy.net/wp-content/uploads/2020/11/Buying-Circular-Saw-Review-300x295.jpg" alt="Buying the best Circular Saw from the Review" width="300" height="295" />There are things that you have to <strong>consider when buying</strong> a circular saw, whether it is a purchase in a physical store or online. Here are some tips for you to use.
<h3>Instore</h3>
<ul>
 	<li>You can decide whether you will buy a cordless or corded circular saw. If you will not use the circular saw for heavy-duty stuff, then you can have a cordless saw that is portable and can be used as needed.</li>
 	<li>What blade you need for the project you will often undertake.</li>
 	<li>You can ask help from the store seller and consult with them what you are planning to do with the circular saw. They will, however, ask some questions to further help you pick the best saw for the job.</li>
 	<li>Blade capacity, what type of blade is there, for what material is it going to be used for, and where you will place, it should be discussed.</li>
 	<li>Check the brands they are carrying and see if there is a free demo for the circular saw as well, so you can have an idea on which is best for your sewing needs.</li>
</ul>
<h3>Online</h3>
If you are to buy a circular saw online, you won't have the advantage of seeing how the saws work, and you will not know if the one you will order will work once it arrives at your doorstep. Here are some tips for when you buy it online.
<ul>
 	<li><strong>Only buy at a trustworthy online seller.</strong> You cannot afford to have a unit that will not only work when you use it, but also the time it will take you to return it and replace it will just be such an inconvenience.</li>
 	<li>Review and compare products online, as there are websites that do these things. You can browse the product online and then compare it with other products. You will get the disadvantage and advantage of each.</li>
 	<li>Rates of products online also help a lot. You will know if such a product or this time a circular saw will be efficient and will not cause you headaches, eventually.</li>
 	<li>Compare prices. Pick the best price from the best online seller.</li>
 	<li>Ask how many years is the warranty good for. Pick the one that will give you a longer warranty time.</li>
 	<li>The return policy should be cleared with the seller. This is important for every transaction that is done online.</li>
</ul>
<h2>FAQ about the Best Circular Saw</h2>
<h3>Do I need to lubricate circular saws?</h3>
<img class="alignright wp-image-4078 size-medium" title="FAQ about the Best Circular Saw" src="https://top-buy.net/wp-content/uploads/2020/11/Questions-Circular-Saw-Review-300x300.jpg" alt="Best Questions about Circular Saws in our Review" width="300" height="300" />Although there is required cleaning and maintenance for most of the circular saws, there are also brands that do not require lubricating parts. Some do. Depend on what<strong> the manual should tell you</strong>, getting some information via the manual should help as well to keep your circular saw working longer.

What are the safety gears used when operating a circular saw? Gloves and eye protection are a good idea to protect you from flying splinters, shards, and wood chips. Make sure that the area you are working on is well lit, has no clutter, and you will not trip, nor fall while you are <strong>doing the sawing and cutting</strong>.
<h3>What are the best circular saws to buy now?</h3>
<ol>
 	<li><strong>Makita Plunge </strong>Circular Saw - Sp6000J1 6-1/2-Inch</li>
 	<li><strong>Dewalt Lightweight</strong> Circular Saw DWE575SB</li>
 	<li><strong>Skilsaw Lightweight </strong>Circular Saw SPT77WML-01</li>
 	<li><strong>Skil 5280-01 </strong>Circular Saw</li>
 	<li><strong>Porter-Cable Heavy Duty </strong>Circular Saw PCE310</li>
</ol>
<h2>Conclusion</h2>
Circular saws have many uses that are highly<strong> important in everyday life</strong>. It has a long-range of uses in building houses, simple projects, a small cabinet, perhaps, or shelves, and all have important functions.[ads2]

<span class="fontstyle0">[box type="success" align="" class="" width=""]</span>Circular saw maybe a piece of the usual equipment to some, but not for those who make a living out of it. Simply put, it is a wise investment.<span class="fontstyle0">[/box]</span>
"""

class Translator_Jomi:
    def __init__(self, text):
        self.text = text
    def clean_strong(self):
        self.text = self.text.replace('<strong>', '').replace('</strong>', '')
        self.text = self.text.replace('<span class="fontstyle0">', '')
        self.text = self.text.replace('</span>', '')
    def clean_a(self):
        output = re.findall('<a href.*</a>', self.text, re.MULTILINE)
        for i in output:
            # Replace </a>
            clean_i = i.replace('</a>', '')
            find_a_start = re.match(r'<a href.*>', clean_i, re.MULTILINE)
            clean_i = clean_i.replace(find_a_start.group(0), '')
            self.text = self.text.replace(i, clean_i)
    def translations(self):
        splited_text = self.text.splitlines()
        translator = google_translator()

        for i in splited_text:
            # Search for image
            search_for_image = re.search(r'<img.*/>', i, re.MULTILINE)

            # Search for shortcode
            search_for_shortcode = re.search(r'\[.*]', i, re.MULTILINE)

            if search_for_image:
                clean_image = i.replace(search_for_image.group(0), '')
                translated = translator.translate(clean_image, lang_tgt='hr')
                soup_trans = BeautifulSoup(translated, "html.parser")
                soup = BeautifulSoup(clean_image, "html.parser")
                text_eng = soup.get_text()
                text_hr = soup_trans.get_text()
                self.text = self.text.replace(text_eng, text_hr)
            elif search_for_shortcode:
                is_box = re.search(r'\[box.*\[/box]', i, re.MULTILINE)
                if is_box:
                    i = i.replace('[/box]', '')
                    remove_box = re.search(r'\[.*]', i, re.MULTILINE)
                    clean_text_box = i.replace(remove_box.group(0), '')
                    translated = translator.translate(clean_text_box, lang_tgt='hr')
                    self.text = self.text.replace(clean_text_box, translated)
                else:
                    i = i.replace(search_for_shortcode.group(0), '')
                    translated = translator.translate(i, lang_tgt='hr')
                    self.text = self.text.replace(i, translated)
            else:
                translated = translator.translate(i, lang_tgt='hr')
                self.text = self.text.replace(i, translated)

        self.text = self.text.replace('</ Ul>', '</ul>')
        self.text = self.text.replace('<Ul>', '<ul>')

text = Translator_Jomi(example_text)

text.clean_a()
text.clean_strong()
text.translations()

print(text.text)
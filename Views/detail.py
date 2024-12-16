import streamlit as st
import pandas as pd
import time

# Title and description 
st.title("✨Explore the Fascinating World of Rice Field Ecosystems")
st.write("Dive into the rich diversity of plant life thriving in rice fields. Discover the unique characteristics of each plant, their impact on the ecosystem, and how they shape the agricultural landscape. Let’s explore the wonders of weedy rice, barnyard grass, and cultivated rice together!")


tab1, tab2 = st.tabs(["Weedy Rice", "Barnyard Grass"])

with tab1:
    st.header("Weedy Rice")
    
    st.subheader("Images:")
    # Expander for the images section
    with st.expander("Images"):
        # Create 3 columns
        col1, col2, col3 = st.columns(3)
        
        # First image in the first column
        with col1:
            st.image("Images/Detail_Image/Weedy_Rice/Weedy_Rice_wb73.JPG", caption="Weedy Rice 1", use_column_width=False, width=300)

        # Second image in the second column
        with col2:
            st.image("Images/Detail_Image/Weedy_Rice/Weedy_Rice_wb90.jpg", caption="Weedy Rice 2", use_column_width=False, width=300)

        # Third image in the third column
        with col3:
            st.image("Images/Detail_Image/Weedy_Rice/Weedy_Rice_wb88.png", caption="Weedy Rice 3", use_column_width=False, width=300)
        
    weedy_rice_description = """
    Weedy rice (Oryza sativa f. spontanea) is a significant invasive weed that closely resembles cultivated rice, making it extremely difficult to control without harming the crop. This similarity, along with its ability to grow taller and have red-pigmented seeds, contributes to its competitiveness in rice fields. Weedy rice plants are often more vigorous than cultivated rice, with longer and narrower leaves, a paler yellowish-green color, and a shorter maturity period. While the seeds appear similar to those of cultivated rice, they may have awns that break off during processing, further complicating differentiation. The difficulty in controlling weedy rice is compounded by its resistance to several herbicides, such as fenoxaprop-P-ethyl and pretilachlor, rendering traditional weed control methods ineffective. As weedy rice continues to interbreed with cultivated rice, it develops herbicide-resistant populations, making management even more challenging. Effective management of weedy rice requires selective control methods that can target these weeds without damaging the rice crop, as weedy rice can significantly reduce yields if left uncontrolled.
    """

    st.subheader("Summary:")
    with st.expander("Summary"):
        st.write(weedy_rice_description)

    # List of characteristics and their descriptions
    characteristics = [
        ["Awned weedy rice seeds", "Weedy rice seeds often have awns that break off during processing, making them difficult to distinguish from cultivated rice."],
        ["Taller than cultivated rice", "Some weedy rice plants grow taller than cultivated rice, which can affect the rice crop's growth and yields."],
        ["Leaf colour (greenish yellow vs green)", "Weedy rice leaves have a paler, yellowish-green color, while cultivated rice leaves are typically a deeper green."],
        ["Stem colour (greenish yellow vs green)", "The stem of weedy rice is usually a paler, greenish-yellow compared to the bright green stem of cultivated rice."],
        ["Reddish-brown husk on seedling", "The husks of weedy rice may be reddish-brown and remain attached to the base of the seedling, further complicating identification."],
        ["Paler leaves", "Weedy rice leaves are usually lighter in color and have a yellowish tint, unlike the darker green leaves of cultivated rice."]
    ]

    # List of corresponding images for each characteristic
    image_paths = [
        "Images/Characteristic_Of_Weedy_Rice/Awned_Weedy_Rice_Seed.png",
        "Images/Characteristic_Of_Weedy_Rice/Taller_Weedy_Rice.png",
        "Images/Characteristic_Of_Weedy_Rice/Leaf_Colour_Weedy_Rice.png",
        "Images/Characteristic_Of_Weedy_Rice/Stem_Colour_Weedy_Rice.png",
        "Images/Characteristic_Of_Weedy_Rice/Reddish_Brown_Husk_Weedy_Rice.png",
        "Images/Characteristic_Of_Weedy_Rice/Paler_Leaves_Weedy_Rice.png"
    ]

    # Loop through each characteristic and image
    st.subheader("Key Characteristics:")

    with st.expander("Key Characteristics"):
        for i, (char, description) in enumerate(characteristics):
            col1, col2 = st.columns([0.2, 0.5], vertical_alignment="center")
            
            with col1:
                st.image(image_paths[i], width=300)
                
            with col2:
                with st.container(border=True):
                    st.write(f"**{char}:**  \n{description}")

    st.subheader("Stages and Characteristics:")
    # Data for the table
    data = {
        "Growth Stage": [
            "Seedling Stage",
            "Vegetative Stage",
            "Reproductive Stage"
        ],
        "Focus Areas": [
            "Skin and size of rice grains",
            "Plant height, leaf colour, leaf size",
            "Height, leaf angle, and size of leaf blades, colour of weedy rice grains"
        ],
        "Morphological Characteristics": [
            "• Weedy rice grains have different colours compared to the cultivar, usually reddish-brown.\n"
            "• The size of weedy rice grains is either larger or smaller than those of the cultivar.",
            
            "• At the beginning of the vegetative stage, weedy rice plants are the same height as the cultivar.\n"
            "• By the end of the vegetative stage, some weedy rice plants begin to grow taller than the cultivar.\n"
            "• The leaf colour of weedy rice is paler (yellowish green) compared to the green leaves of the cultivar.\n"
            "• The leaves of weedy rice are longer and narrower.\n"
            "• The leaf blades of the weedy rice are erect like those of the cultivar.",
            
            "• At this stage, there are weedy rice plants that are taller than the cultivar.\n"
            "• The angles of the leaf blades of weedy rice are mostly inclined, while the leaf blades of the cultivar are erect (except for the UKMRC variety, which has inclined leaf blades like weedy rice).\n"
            "• The colour of weedy rice grains is different from the cultivar, usually reddish-brown when the grain skin is still wet in the morning.\n"
            "• Some weedy rice grains may be awned."
        ]
    }

    # Creating the DataFrame
    df = pd.DataFrame(data)

    # Display the table 
    with st.expander("Stages and Characteristics"):
        st.table(df)
        st.markdown("**Source:** Vun et al., 2021")
    
with tab2:
    st.header("Barnyard Grass")
    
    st.subheader("Images:")
    # Expander for the images section
    with st.expander("Images"):
        # Create 3 columns
        col1, col2, col3 = st.columns(3)
        
        # First image in the first column
        with col1:
            st.image("Images/barnyard_grass.jpg", caption="Barnyard Grass 1", use_column_width=False, width=300)

        # Second image in the second column
        with col2:
            st.image("Images/Detail_Image/Barnyard_Grass/Barnyard_Grass_215.png", caption="Barnyard Grass 2", use_column_width=False, width=300)

        # Third image in the third column
        with col3:
            st.image("Images/Detail_Image/Barnyard_Grass/Barnyard_Grass_283.png", caption="Barnyard Grass 3", use_column_width=False, width=300)
        
    weedy_rice_description = """
    Barnyard Grass (*Echinochloa crus-galli*) is a fast-growing, annual grass species native to Asia but now widespread globally due to its adaptability. Commonly found in agricultural fields, particularly rice paddies, as well as moist or disturbed environments, this weed thrives in warm, wet climates and poorly drained soils. It has coarse, upright growth, long flat leaves, purple-tinged stems, and a distinctive seed head resembling a spike, producing numerous small, brownish seeds. Barnyard grass poses a significant threat to agriculture by competing with crops like rice for sunlight, nutrients, and water, often reducing yields. Its rapid growth and ability to develop herbicide resistance make it a challenging weed to control. Management strategies include cultural practices like crop rotation and water management, mechanical methods such as hand weeding or tilling, and the use of selective herbicides, though resistance management is critical. Biological control options are also under research to address its persistent impact.
    """

    st.subheader("Summary:")
    with st.expander("Summary"):
        st.write(weedy_rice_description)

    # List of characteristics and their descriptions
    characteristics = [
        ["Erect and vigorous growth", "Barnyard grass is an erect, vigorous, bright-green, summer-active grass that can grow as tall as 120 cm in good conditions."],
        ["Flower stems and branching", "Flower stems are stout, prostrate at the base and upright when flowering. Stems are often branched and are hairless between the nodes."],
        ["Leaf blade characteristics", "Leaf blades are flat, soft, usually hairless, 15-50 cm long and 5-15 mm wide. There is no ligule at the base of the leaf blade."],
        ["Seed head structure", "Seed head is an erect panicle, 10-20 cm long, with 10-20 branches (racemes), each up to 6 cm long. Those at the base are longer than those at the top."],
        ["Raceme and spikelet features", "Racemes are densely packed with spikelets of awned seed (occasionally the awns are very short), green or purple in colour."],
        ["Spikelet arrangement and florets", "Spikelets are crowded in twos or threes on one side of the axis. Each falls entire at maturity, 3-5 mm long, with two florets, the lower barren the upper bisexual."]
    ]

    # List of corresponding images for each characteristic
    image_paths = [
        "Images/Characteristic_Of_Barnyard_Grass/Barnyard_Grass_100.png",
        "Images/Characteristic_Of_Barnyard_Grass/Barnyard_Grass_129.png",
        "Images/Characteristic_Of_Barnyard_Grass/Barnyard_Grass_141.png",
        "Images/Characteristic_Of_Barnyard_Grass/Barnyard_Grass_142.png",
        "Images/Characteristic_Of_Barnyard_Grass/Barnyard_Grass_147.png",
        "Images/Characteristic_Of_Barnyard_Grass/Barnyard_Grass_248.png"
    ]

    # Loop through each characteristic and image
    st.subheader("Key Characteristics:")

    with st.expander("Key Characteristics"):
        for i, (char, description) in enumerate(characteristics):
            col1, col2 = st.columns([0.2, 0.5], vertical_alignment="center")
            
            with col1:
                st.image(image_paths[i], width=300)
                
            with col2:
                with st.container(border=True):
                    st.write(f"**{char}:**  \n{description}")

    st.subheader("Stages and Characteristics:")
    # Data for the table
    data = {
        "Growth Stage": [
            "Seedling Stage",
            "Vegetative Stage",
            "Reproductive Stage"
        ],
        "Focus Areas": [
            "Leaf blades and early stem development",
            "Plant height, leaf characteristics, and stem branching",
            "Seed head structure and spikelet arrangement"
        ],
        "Morphological Characteristics": [
            "• Barnyard grass seedlings have flat, soft, and usually hairless leaf blades.\n"
            "• Leaves are bright green and 15-50 cm long, with no ligule at the base.",
            
            "• During the vegetative stage, barnyard grass exhibits vigorous growth, reaching heights up to 120 cm in good conditions.\n"
            "• Stems are prostrate at the base and upright when flowering, often branched and hairless between nodes.\n"
            "• Leaves remain flat, soft, and bright green, with a length of 15-50 cm and a width of 5-15 mm.",
            
            "• At this stage, barnyard grass develops an erect panicle as its seed head, measuring 10-20 cm long with 10-20 racemes.\n"
            "• Racemes are densely packed with spikelets that are green or purple in color, and awned (occasionally with very short awns).\n"
            "• Spikelets are crowded in twos or threes on one side of the axis, with two florets, the lower barren and the upper bisexual."
        ]
    }

    # Creating the DataFrame
    df = pd.DataFrame(data)

    # Display the table 
    with st.expander("Stages and Characteristics"):
        st.table(df)
        st.markdown("**Source:** [Barnyard Grass - AgPest](https://agpest.co.nz/?pesttypes=barnyard-grass)")
def create_deforestation_message():
    """
    Generates a general message about deforestation.
    :return:
    The message generated
    """
    print("Deforestation is a serious environmental issue. Help save our forests!")


create_deforestation_message()

def create_deforestation_message(location, message="Deforestation is a serious environmental issue.\nHelp save our forests!"):
    """
    Generates a general message about deforestation.

    :param location: str, the location affected by deforestation
    :param message: str, the message to convey (default is a general message)
    :return:
    """
    print(f"Deforestation in {location}: {message}")

create_deforestation_message('Amazon Rainforest')
create_deforestation_message('Borneo', 'Preserve biodiversity!')

def create_deforestation_message(location,message= "Deforestation is a serious environmental issue.\nHelp save our forests!"):
    """
    Generates a general message about deforestation.
    :param location: str, the location affected by deforestation
    :param message: str, the message to convey (default is the general message)
    :return:
    """
    print(f"Deforstation in {location}: {message}")
create_deforestation_message(message="Preserve biodiversity!", location="Borneo")
create_deforestation_message("Borneo","Preserve biodiversity!")
create_deforestation_message("Preserve biodiversity", "Borneo")

def create_deforestation_impact (*consequences):
    """
    Describes the impacts of deforestation.
    :param consequences: tuple, variable number of consequences
    :return:
    """
    print("Impacts of deforestation:")
    print(",".join(consequences))
create_deforestation_impact("Loss of biodiversity","Climate change","Disruption of ecosystems")

def list_forest_details(**details):
    """
    Lists detailed informtion about a forest.
    :param details: dict, variable number of keyword arguments
    :return:
    """
    print("Forest details")
#Call the list_forest_details function and pass it various forest details
    for key, value in details.items():
        print(f"{key}: {value}")
list_forest_details(location="Borneo", cause="Illegal logging", area="National Park")

def calculate_deforestation_impact(initial_forest_area, remaining_forest_area, carbon_emission_factor=2.3):
    """
    Calculates the impact of deforestation.
    :param initial_forest_area: float, initial forest area in square kilometres
    :param remaining_forest_area: float, remaining forest area in square kilometres
    :param carbon_emission_factor: float, factor representing Co2 emissions per unit of tree cover loss(default is 2.3)
    :return: (float, float, float), percentage of tree cover loss,remaining forest area, and estimated increase in Co2 emissions
    """
    tree_cover_loss_percentage = ((initial_forest_area - remaining_forest_area) / initial_forest_area) * 100
    estimated_emission = tree_cover_loss_percentage * carbon_emission_factor * initial_forest_area / 100
    return tree_cover_loss_percentage, remaining_forest_area, estimated_emission


loss_percentage, remaining_area, co2_increase = calculate_deforestation_impact(1000,800)
print(f"Tree cover loss percentage: {loss_percentage}")
print(f"Remaining forest area: {remaining_area} square kilometres")
print(f"Estimated increase in CO2 emissions: {co2_increase} metric tons")
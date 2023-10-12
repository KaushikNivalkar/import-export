
def plan_exist_or_create(data):
    print("--------------plan update create--------------------")
    insurer = Insurer.objects.get(slug = data.get("insurer_slug"))
    healthproduct, created = HealthProduct.objects.update_or_create(
        slug = data.get("slug"),
    defaults = {
        'title': data.get("title"),
        'insurer' : insurer,
        'plan_type': data.get("plan_type"),
        'policy_type': data.get("policy_type"),
        'coverage_category': data.get("coverage_category"),
        'policy_wordings': data.get("policy_wordings"),
        'brochure': data.get("brochure"),
        'notes': data.get("notes"),
        'is_proposer_always_insured': data.get("is_proposer_always_insured"),
        'are_parents_allowed_with_proposer': data.get("are_parents_allowed_with_proposer"),
        'are_parents_disallowed': data.get("are_parents_disallowed"),
        'is_completed': data.get("is_completed"),
        'is_backend_integrated': data.get("is_backend_integrated"),
        'faqs': data.get("faqs"),
        'usps': data.get("usps"),
        'short_description': data.get("short_description"),
        'long_description': data.get("long_description"),
        'brand_page_slug': data.get("brand_page_slug"),
        'meta_title': data.get("meta_title"),
        'meta_description': data.get("meta_description")
    }
    )
    print(f"----------health product: {healthproduct.slug} - created :{created}")
    return healthproduct

#

def get_attr_for_db(db_feature_mapping, feature, slab_json):
    f = db_feature_mapping.get(feature)
    if f:
        return f.get(slab_json[feature])
    return None


def slab_update_or_create(slab_json, db_feature_mapping, zrr_to_db_mapping, health_product):
    obj, created = Slab.all_objects.update_or_create(
    sum_assured = slab_json["sum_assured"], 
                    deductible = slab_json["deductible"], 
                    health_product = health_product, grade = slab_json["grade"],
    defaults= {
        "yearly_discounts": db_feature_mapping["yearly_discounts"].get(slab_json["yearly_discounts"]),
        "general": db_feature_mapping["general"].get(slab_json["general"]),
        "dental_coverage": db_feature_mapping["dental_coverage"].get(slab_json["dental_coverage"]),
        "family_coverage": db_feature_mapping["family_coverage"].get(slab_json["family_coverage"]),
        "network_hospital_daily_cash": db_feature_mapping["network_hospital_daily_cash"].get(slab_json["network_hospital_daily_cash"]),
        "ambulance_charges": db_feature_mapping["ambulance_charges"].get(slab_json["ambulance_charges"]),
        "alternative_practices_coverage": db_feature_mapping["alternative_practices_coverage"].get(slab_json["alternative_practices_coverage"]),
        "pre_existing": db_feature_mapping["pre_existing"].get(slab_json["pre_existing"]),
        "maternity_cover": db_feature_mapping["maternity_cover"].get(slab_json["maternity_cover"]),
        "eye_coverage": db_feature_mapping["eye_coverage"].get(slab_json["eye_coverage"]),
        "day_care": db_feature_mapping["day_care"].get(slab_json["day_care"]),
        "age_limit": db_feature_mapping["age_limit"].get(slab_json["age_limit"]),
        "online_availability": db_feature_mapping["online_availability"].get(slab_json["online_availability"]),
        "medical_required": db_feature_mapping["medical_required"].get(slab_json["medical_required"]),
        "standard_exclusion": db_feature_mapping["standard_exclusion"].get(slab_json["standard_exclusion"]),
        "domiciliary_hospitalization": db_feature_mapping["domiciliary_hospitalization"].get(slab_json["domiciliary_hospitalization"]),
        "bonus": db_feature_mapping["bonus"].get(slab_json["bonus"]),
        "premium_discount": db_feature_mapping["premium_discount"].get(slab_json["premium_discount"]),
        "convalescence_benefit": db_feature_mapping["convalescence_benefit"].get(slab_json["convalescence_benefit"]),
        "non_network_hospital_daily_cash": db_feature_mapping["non_network_hospital_daily_cash"].get(slab_json["non_network_hospital_daily_cash"]),
        "pre_post_hospitalization": db_feature_mapping["pre_post_hospitalization"].get(slab_json["pre_post_hospitalization"]),
        "copay": db_feature_mapping["copay"].get(slab_json["copay"]),
        "health_checkup": db_feature_mapping["health_checkup"].get(slab_json["health_checkup"]),
        "claims": db_feature_mapping["claims"].get(slab_json["claims"]),
        "outpatient_benefits": db_feature_mapping["outpatient_benefits"].get(slab_json["outpatient_benefits"]),
        "organ_donor": db_feature_mapping["organ_donor"].get(slab_json["organ_donor"]),
        "life_long_renewability": db_feature_mapping["life_long_renewability"].get(slab_json["life_long_renewability"]),
        "critical_illness_coverage": db_feature_mapping["critical_illness_coverage"].get(slab_json["critical_illness_coverage"]),
        "restore_benefits": db_feature_mapping["restore_benefits"].get(slab_json["restore_benefits"]),
        "special_feature": db_feature_mapping["special_feature"].get(slab_json["special_feature"]),
        "waiting_period_at_inception_of_ci": None,
        "survival_period_for_ci_after_diagnosis": None,
        "is_active": True
    }
)
    print(f"-------slab {obj.sum_assured} - {obj.deductible} : created : {created}")
    for zrr in slab_json.get("zrrs"):
        obj.zonal_room_rent.add(zrr_to_db_mapping[zrr])


# Create a mapping of model names to model classes
model_mapping = {
    'general': "General",
    'pre_existing': "PreExisting",
    'yearly_discounts': "YearlyDiscounts",
    'dental_coverage': "DentalCoverage",
    'family_coverage': "FamilyCoverage",
    'network_hospital_daily_cash': "NetworkHospitalDailyCash",
    'ambulance_charges': "AmbulanceCharges",
    'alternative_practices_coverage': "AlternativePracticesCoverage",
    'maternity_cover':"MaternityCover",
    'eye_coverage':"EyeCoverage",
    'day_care':"DayCare",
    'age_limit':"AgeLimit",
    'online_availability':"OnlineAvailability",
    'medical_required':"MedicalRequired",
    'standard_exclusion':"StandardExclusion",
    'domiciliary_hospitalization':"DomiciliaryHospitalization",
    'bonus':"Bonus",
    'premium_discount':"PremiumDiscount",
    'convalescence_benefit':"ConvalescenceBenefit",
    'non_network_hospital_daily_cash':"NonNetworkHospitalDailyCash",
    'pre_post_hospitalization':"PrePostHospitalization",
    'copay':"Copay",
    'health_checkup':"HealthCheckup",
    'outpatient_benefits':"OutpatientBenefits",
    'organ_donor':"OrganDonor",
    'life_long_renewability':"LifeLongRenewability",
    'critical_illness_coverage':"CriticalIllnessCoverage",
    'restore_benefits':"RestoreBenefits",
    'special_feature':"SpecialFeature",
    'claims': "Claims"
}
# Create a dictionary to store the model objects

def feature_to_db_mapping(features):
    from django.apps import apps
    db_feature_mapping = {}
    # Iterate through the 'features' dictionary and create model objects
    for model_name, item_data in features.items():
        model_class = model_mapping.get(model_name)

        # get models from wiki through model_mapping
        MyModel = apps.get_model("wiki", model_class)
        if MyModel:
            for item_id, item_attributes in item_data.items():   #TODO: if items_data in None
                print(item_id, item_attributes)
                if item_attributes:
                # Create a model instance with the provided attributes
                    model_instance = MyModel(**item_attributes)
                    # model_instance.save()
                else:
                    model_instance = None
                # Add the model instance to the db_feature_mapping dictionary
                db_feature_mapping.setdefault(model_name, {})[item_id] = model_instance
    return db_feature_mapping

def zrr_to_db(zrr):
    zrr_to_db_mapping = {}
    for zrr_key,zrr_value in zrr.items():
        z = ZonalRoomRent(**zrr_value)
        z.save()
        zrr_to_db_mapping[zrr_key] = z
    return zrr_to_db_mapping
        
def import_plan(data):
    health_product = plan_exist_or_create(data)
    if health_product:
        features = data.get("features")
        zrr = data.get("zonal_room_rent")
        db_feature_mapping = feature_to_db_mapping(features)
        zrr_to_db_mapping = zrr_to_db(zrr)
        slabs = data.get("slabs")
        for slab in slabs:
            slab_update_or_create(slab, db_feature_mapping, zrr_to_db_mapping, health_product)

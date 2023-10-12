
from wiki.models import *


def serialize_health_product(product):
    return {
        "insurer_slug":product.insurer.slug,
        "title": product.title,
        "slug": product.slug,
        "plan_type": product.plan_type,
        "policy_type": product.policy_type,
        "slabs": [],
        "coverage_category": product.coverage_category,
        "author_id": {"author_dict": {}},
        "notes": product.notes,
        "is_proposer_always_insured": product.is_proposer_always_insured,
        "are_parents_allowed_with_proposer": product.are_parents_allowed_with_proposer,
        "are_parents_disallowed": product.are_parents_disallowed,
        "is_completed": product.is_completed,
        "is_backend_integrated": product.is_backend_integrated,
        "faqs": product.faqs,
        "usps": product.usps,
        "short_description": product.short_description,
        "brand_page_slug": product.brand_page_slug,
        "meta_title": product.meta_title,
        "meta_description": product.meta_description,
        "features": "",
        "zonal_room_rent":[],
        "upload_premium_files": []
    }


def serialize_yearly_discounts(yearly_discount):
    if yearly_discount:
        return {
            'two_year_discount': yearly_discount.two_year_discount,
            'three_year_discount': yearly_discount.three_year_discount
        }


def serialize_general(general):
    if general:
        return {
            'waiting_period': general.waiting_period,
            'portability': general.portability
        }


def serialize_dental_coverage(dental_coverage):
    if dental_coverage:
        return {
            'condition': dental_coverage.condition,
            'copay': dental_coverage.copay,
            'limit': dental_coverage.limit,
            'waiting_period': dental_coverage.waiting_period,
        }


def serialize_family_coverage(family_coverage):
    if family_coverage:
        return {
            'number_of_maximum_members': family_coverage.number_of_maximum_members,
            'maximum_dependent_age': family_coverage.maximum_dependent_age,
            'is_maximum_dependent_age_inclusive': family_coverage.is_maximum_dependent_age_inclusive
        }


def serialize_network_hospital_daily_cash(network_hospital_daily_cash):
    if network_hospital_daily_cash:
        return {
            'is_available': network_hospital_daily_cash.is_available,
            'condition': network_hospital_daily_cash.condition,
            'is_icu_available': network_hospital_daily_cash.is_icu_available,
            'limit_per_day_allowance_icu': network_hospital_daily_cash.limit_per_day_allowance_icu,
            'limit_per_day_allowance': network_hospital_daily_cash.limit_per_day_allowance,
            'limit_cummulative_allowance': network_hospital_daily_cash.limit_cummulative_allowance,
            'from_day': network_hospital_daily_cash.from_day,
            'to_day': network_hospital_daily_cash.to_day,
            'number_of_days': network_hospital_daily_cash.number_of_days
        }


def serialize_critical_illness_coverage(critical_illness_coverage):
    if critical_illness_coverage:
        return {
            'is_available': False,
            'limit': None,
            'limit_in_percentage': None,
            'included_in_plan': None,
            'benefit_type': ''
        }


def serialize_ambulance_charges(ambulance_charges):
    if ambulance_charges:
        return {
            'condition': ambulance_charges.condition,
            'is_ambulance_services_covered': ambulance_charges.is_ambulance_services_covered,
            'limit_in_network_hospitals': ambulance_charges.limit_in_network_hospitals,
            'limit_in_non_network_hospitals': ambulance_charges.limit_in_non_network_hospitals,
            'max_limit_in_network_hospitals': ambulance_charges.max_limit_in_network_hospitals,
            'max_limit_in_non_network_hospitals': ambulance_charges.max_limit_in_non_network_hospitals

        }


def serialize_alternative_practices_coverage(alternative_practices_coverage):
    if alternative_practices_coverage:
        return {
            'limit_in_percentage': alternative_practices_coverage.limit_in_percentage,
            'limit': alternative_practices_coverage.limit
        }


def serialize_pre_existing(pre_existing):
    if pre_existing:
        return {
            'waiting_period': pre_existing.waiting_period,
            'portability': pre_existing.portability
        }


def serialize_maternity_cover(maternity_cover):
    if maternity_cover:
        return {
            'is_covered': maternity_cover.is_covered,
            'waiting_period': maternity_cover.waiting_period,
            'limit_for_normal_delivery': maternity_cover.limit_for_normal_delivery,
            'limit_for_cesarean_delivery': maternity_cover.limit_for_cesarean_delivery,
            'delivery_limit': maternity_cover.delivery_limit
        }


def serialize_eye_coverage(eye_coverage):
    if eye_coverage:
        return {
            'condition': eye_coverage.condition,
            'copay': eye_coverage.copay,
            'limit': eye_coverage.limit,
            'waiting_period': eye_coverage.waiting_period,
        }


def serialize_day_care(day_care):
    if day_care:
        return {
            'is_covered': day_care.is_covered,
            'defined_list': day_care.defined_list,
            'number_of_covered_procedures': day_care.number_of_covered_procedures,
        }


def serialize_age_limit(age_limit):
    if age_limit:
        return {
            'minimum_entry_age': age_limit.minimum_entry_age,
            'maximum_entry_age': age_limit.maximum_entry_age,
            'exceptional_age_config': age_limit.exceptional_age_config
        }


def serialize_online_availability(online_availability):
    if online_availability:
        return {
            'is_available_online': online_availability.is_available_online,
            'maximum_age': online_availability.maximum_age
        }


def serialize_medical_required(medical_required):
    if medical_required:
        return {
            'is_medical_required': medical_required.is_medical_required,
            'maximum_age': medical_required.maximum_age
        }


def serialize_standard_exclusion(standard_exclusion):
    if standard_exclusion:
        return {

        }


def serialize_domiciliary_hospitalization(domiciliary_hospitalization):
    if domiciliary_hospitalization:
        return {
            'is_covered': domiciliary_hospitalization.is_covered,
            'limit': domiciliary_hospitalization.limit,
            'limit_in_percentage': domiciliary_hospitalization.limit_in_percentage
        }


def serialize_bonus(bonus):
    if bonus:
        return {
            'is_available': bonus.is_available,
            'unclaimed_years': bonus.unclaimed_years,
            'bonus_amount': bonus.bonus_amount,
            'maximum_bonus_amount': bonus.maximum_bonus_amount,
            'maximum_years': bonus.maximum_years,
            'reduction_in_bonus_amount_after_claim': bonus.reduction_in_bonus_amount_after_claim,
            'bonus_calculation_method': bonus.bonus_calculation_method
        }


def serialize_premium_discount(premium_discount):
    if premium_discount:
        return {
            'is_available': premium_discount.is_available,
            'unclaimed_years': premium_discount.unclaimed_years,
            'discount_amount': premium_discount.discount_amount,
            'maximum_discount_amount': premium_discount.maximum_discount_amount,
            'maximum_years': premium_discount.maximum_years,
            'reduction_in_discount_amount_after_claim': premium_discount.reduction_in_discount_amount_after_claim,
            'discount_calculation_method': premium_discount.discount_calculation_method
        }


def serialize_convalescence_benefit(convalescence_benefit):
    if convalescence_benefit:
        return {
            'condition': convalescence_benefit.condition,
            'limit': convalescence_benefit.limit,
            'minimum_days_of_hospitalization': convalescence_benefit.minimum_days_of_hospitalization,
            'amount_per_day': convalescence_benefit.amount_per_day,
            'maximum_number_of_days': convalescence_benefit.maximum_number_of_days
        }


def serialize_non_network_hospital_daily_cash(non_network_hospital_daily_cash):
    if non_network_hospital_daily_cash:
        return {
            'is_available': non_network_hospital_daily_cash.is_available,
            'condition': non_network_hospital_daily_cash.condition,
            'is_icu_available': non_network_hospital_daily_cash.is_icu_available,
            'limit_per_day_allowance_icu': non_network_hospital_daily_cash.limit_per_day_allowance_icu,
            'limit_per_day_allowance': non_network_hospital_daily_cash.limit_per_day_allowance,
            'limit_cummulative_allowance': non_network_hospital_daily_cash.limit_cummulative_allowance,
            'from_day': non_network_hospital_daily_cash.from_day,
            'to_day': non_network_hospital_daily_cash.to_day,
            'number_of_days': non_network_hospital_daily_cash.number_of_days
        }


def serialize_pre_post_hospitalization(pre_post_hospitalization):
    if pre_post_hospitalization:
        return {
            'is_available': pre_post_hospitalization.is_available,
            'intimation_time': pre_post_hospitalization.intimation_time,
            'days_pre_hospitalization': pre_post_hospitalization.days_pre_hospitalization,
            'days_post_hospitalization': pre_post_hospitalization.days_post_hospitalization,
            'days_pre_hospitalization_with_intimation': pre_post_hospitalization.days_pre_hospitalization_with_intimation,
            'days_post_hospitalization_with_intimation': pre_post_hospitalization.days_post_hospitalization_with_intimation,
            'cummulative_limit': pre_post_hospitalization.cummulative_limit,
            'cummulative_limit_in_percentage': pre_post_hospitalization.cummulative_limit_in_percentage
        }


def serialize_copay(copay):
    if copay:
        return {
            "is_available": copay.is_available,
            "applicable_after_age": copay.applicable_after_age,
            "applicable_after_entry_age": copay.applicable_after_entry_age,
            "age_copay_network_hospital": copay.age_copay_network_hospital,
            "age_copay_non_network_hospital": copay.age_copay_non_network_hospital,
            "for_network_hospital": copay.for_network_hospital,
            "for_non_network_hospital": copay.for_non_network_hospital,
            "on_day_care_for_network_hospital": copay.on_day_care_for_network_hospital,
            "on_day_care_for_non_network_hospital": copay.on_day_care_for_non_network_hospital
        }


def serialize_health_checkup(health_checkup):
    if health_checkup:
        return {
            'is_available': health_checkup.is_available,
            'waiting_period': health_checkup.waiting_period,
            'limit_in_percentage': health_checkup.limit_in_percentage,
            'limit': health_checkup.limit,
            'is_claim_free_required': health_checkup.is_claim_free_required,
            'is_fixed_set_tests': health_checkup.is_fixed_set_tests
        }


def serialize_claims(claims):
    if claims:
        return {
            'service_promise': claims.service_promise,
            'tat_commited': claims.tat_commited,
            'tat_commited_penalty': claims.tat_commited_penalty,
            'intimation_for_cashless': claims.intimation_for_cashless,
            'intimation_for_emergency': claims.intimation_for_emergency
        }


def serialize_outpatient_benefits(outpatient_benefits):
    if outpatient_benefits:
        return {
            'is_covered': outpatient_benefits.is_covered,
            'number_of_consultations': outpatient_benefits.number_of_consultations,
            'limit': outpatient_benefits.limit
        }


def serialize_organ_donor(organ_donor):
    if organ_donor:
        return {
            'is_covered': organ_donor.is_covered,
            'is_surgery_covered': organ_donor.is_surgery_covered,
            'limit': organ_donor.limit,
            'limit_in_percentage': organ_donor.limit_in_percentage
        }


def serialize_life_long_renewability(life_long_renewability):
    if life_long_renewability:
        return {
            'condition': life_long_renewability.condition,
            'age_limit': life_long_renewability.age_limit
        }


def serialize_restore_benefits(restore_benefits):
    if restore_benefits:
        return {
            'is_available': restore_benefits.is_available,
            'amount_restored': restore_benefits.amount_restored,
            'amount_restored_percentage': restore_benefits.amount_restored_percentage
        }


def serialize_special_feature(special_feature):
    if special_feature:
        return {
            'feature': special_feature.feature
        }


def serialize_cover_premium_table(cover_premium_table):
    if cover_premium_table:
        return {
            'payment_period': cover_premium_table.payment_period,
            'lower_age_limit': cover_premium_table.lower_age_limit,
            'upper_age_limit': cover_premium_table.upper_age_limit,
            'gender': cover_premium_table.gender,
            'base_premium': cover_premium_table.base_premium,
            'service_tax': cover_premium_table.service_tax,
            '_premium': cover_premium_table._premium,
            'is_active': cover_premium_table.is_active,
            'two_year_discount': cover_premium_table.two_year_discount
        }

def serialize_zonal_room_rent(zonal_room_rent):
    if zonal_room_rent:
        return{
            'conditions': zonal_room_rent.conditions,
            'room_available': zonal_room_rent.room_available,
            'limit_daily': zonal_room_rent.limit_daily,
            'limit_daily_in_percentage': zonal_room_rent.limit_daily_in_percentage,
            'limit_daily_in_icu': zonal_room_rent.limit_daily_in_icu,
            'limit_daily_in_percentage_in_icu': zonal_room_rent.limit_daily_in_percentage_in_icu,
            'limit_maximum_total': zonal_room_rent.limit_maximum_total,
            'limit_maximum_total_in_icu': zonal_room_rent.limit_maximum_total_in_icu
        }

def serialize_slab(slab):
    return {
        'sum_assured': slab.sum_assured,
        'deductible': slab.deductible,
        'grade': slab.grade,
        'yearly_discounts': slab.yearly_discounts.id if slab.yearly_discounts else None,
        'general': slab.general.id if slab.general else None,
        'dental_coverage': slab.dental_coverage.id if slab.dental_coverage else None,
        'family_coverage': slab.family_coverage.id if slab.family_coverage else None,
        'network_hospital_daily_cash': slab.network_hospital_daily_cash.id if slab.network_hospital_daily_cash else None,
        'ambulance_charges': slab.ambulance_charges.id if slab.ambulance_charges else None,
        'alternative_practices_coverage': slab.alternative_practices_coverage.id if slab.alternative_practices_coverage else None,
        'pre_existing': slab.pre_existing.id if slab.pre_existing else None,
        'maternity_cover': slab.maternity_cover.id if slab.maternity_cover else None,
        'eye_coverage': slab.eye_coverage.id if slab.eye_coverage else None,
        'day_care': slab.day_care.id if slab.day_care else None,
        'age_limit': slab.age_limit.id if slab.age_limit else None,
        'online_availability': slab.online_availability.id if slab.online_availability else None,
        'medical_required': slab.medical_required.id if slab.medical_required else None,
        'standard_exclusion': slab.standard_exclusion.id if slab.standard_exclusion else None,
        'domiciliary_hospitalization': slab.domiciliary_hospitalization.id if slab.domiciliary_hospitalization else None,
        'bonus': slab.bonus.id if slab.bonus else None,
        'premium_discount': slab.premium_discount.id if slab.premium_discount else None,
        'convalescence_benefit': slab.convalescence_benefit.id if slab.convalescence_benefit else None,
        'non_network_hospital_daily_cash': slab.non_network_hospital_daily_cash.id if slab.non_network_hospital_daily_cash else None,
        'pre_post_hospitalization': slab.pre_post_hospitalization.id if slab.pre_post_hospitalization else None,
        'copay': slab.copay.id if slab.copay else None,
        'health_checkup': slab.health_checkup.id if slab.health_checkup else None,
        'claims': slab.claims.id if slab.claims else None,
        'outpatient_benefits': slab.outpatient_benefits.id if slab.outpatient_benefits else None,
        'organ_donor': slab.organ_donor.id if slab.organ_donor else None,
        'life_long_renewability': slab.life_long_renewability.id if slab.life_long_renewability else None,
        'critical_illness_coverage': slab.critical_illness_coverage.id if slab.critical_illness_coverage else None,
        'restore_benefits': slab.restore_benefits.id if slab.restore_benefits else None,
        'special_feature': slab.special_feature.id if slab.special_feature else None,
        'waiting_period_at_inception_of_ci': slab.waiting_period_at_inception_of_ci,
        'survival_period_for_ci_after_diagnosis': slab.survival_period_for_ci_after_diagnosis,
        'is_active': slab.is_active,
        'zrrs': [zrr.id for zrr in slab.zonal_room_rent.all()]
    }

function_mapping = {'general': serialize_general,
 'pre_existing': serialize_pre_existing,
 'yearly_discounts': serialize_yearly_discounts,
 'dental_coverage': serialize_dental_coverage,
 'family_coverage': serialize_family_coverage,
 'network_hospital_daily_cash': serialize_network_hospital_daily_cash,
 'ambulance_charges': serialize_ambulance_charges,
 'alternative_practices_coverage': serialize_alternative_practices_coverage,
 'maternity_cover': serialize_maternity_cover,
 'eye_coverage': serialize_eye_coverage,
 'day_care': serialize_day_care,
 'age_limit': serialize_age_limit,
 'online_availability': serialize_online_availability,
 'medical_required': serialize_medical_required,
 'standard_exclusion': serialize_standard_exclusion,
 'domiciliary_hospitalization': serialize_domiciliary_hospitalization,
 'bonus': serialize_bonus,
 'premium_discount': serialize_premium_discount,
 'convalescence_benefit': serialize_convalescence_benefit,
 'non_network_hospital_daily_cash': serialize_non_network_hospital_daily_cash,
 'pre_post_hospitalization': serialize_pre_post_hospitalization,
 'copay': serialize_copay,
 'health_checkup': serialize_health_checkup,
 'outpatient_benefits': serialize_outpatient_benefits,
 'organ_donor': serialize_organ_donor,
 'life_long_renewability': serialize_life_long_renewability,
 'critical_illness_coverage': serialize_critical_illness_coverage,
 'restore_benefits': serialize_restore_benefits,
 'special_feature': serialize_special_feature,
 'claims': serialize_claims,
 }

def call_functions(func_name, para):  
    func = function_mapping.get(func_name)
    if func:
        result = func(para)
    else:
        result = f"Function '{func_name}' not found"
    return result

    

def get_rate_chart(health_product_slug):
    import requests
    rate_chart_urls = []
    for up in UploadPremium.objects.all():
        try:
            print("-----------------------------",up.file.url)
            res = requests.get(up.file.url)
            if res.status_code == 200:
                if health_product_slug in res.text:
                    rate_chart_urls.append(up.file.url)
            
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
    return rate_chart_urls

def one_export(h):
    zrr_dict_mapping = {}
    h_ser = serialize_health_product(h)
    # h_ser["upload_premium_files"] = get_rate_chart(h.slug)
    feature = {
        'general': {},
        'pre_existing': {},
        'yearly_discounts': {},
        'dental_coverage': {},
        'family_coverage': {},
        'network_hospital_daily_cash': {},
        'ambulance_charges': {},
        'alternative_practices_coverage': {},
        'maternity_cover': {},
        'eye_coverage': {},
        'day_care': {},
        'age_limit': {},
        'online_availability': {},
        'medical_required': {},
        'standard_exclusion': {},
        'domiciliary_hospitalization': {},
        'bonus': {},
        'premium_discount': {},
        'convalescence_benefit': {},
        'non_network_hospital_daily_cash': {},
        'pre_post_hospitalization': {},
        'copay': {},
        'health_checkup': {},
        'outpatient_benefits': {},
        'organ_donor': {},
        'life_long_renewability': {},
        'critical_illness_coverage': {},
        'restore_benefits': {},
        'special_feature': {},
        'claims': {},
    }
    slabs = Slab.objects.filter(health_product=h)
    for s in slabs:

        ser = serialize_slab(s)
        for key in feature.keys():
            attr = getattr(s, key)
            if attr and attr.id not in feature[key]:
                json_feature = call_functions(key,attr)
                feature[key][attr.id] = json_feature

        h_ser["slabs"].append(ser)
        h_ser["features"] = feature

    zrr = ZonalRoomRent.objects.filter(slabs__health_product = h)
    for z in zrr:
        zrr_dict_mapping[z.id] = serialize_zonal_room_rent(z)

    h_ser["zonal_room_rent"] = zrr_dict_mapping

    print(f"--------{h.slug}----{h_ser}")
    return h_ser

#----------------passed the slug here and call one_export() ------------------
#---------------replace 
one_hp = HealthProduct.objects.get(slug = "royal-sundaram-lifeline-individual")
data = one_export(one_hp)

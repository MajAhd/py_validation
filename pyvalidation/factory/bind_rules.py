import pyvalidation.rules as Rules


class BindRules:
    """
     Bind Validation Rules from /rules
     :param rule validate name and the rule of validate
     :param rule_val validate default value ro further process
     :param all_data all data inside the validation request
    """

    def __init__(self, rule, rule_val, all_data):
        self.rule = rule
        self.rule_val = rule_val
        self.all_data = all_data

    def build(self, key, value):
        """
        base on rule bind and run validation
        :param key: data name
        :param value: data value
        :return: Boolean
        """
        match self.rule:
            case "required":
                return Rules.Required(value).is_required()
            case _:
                return "Validation Not Defined!"

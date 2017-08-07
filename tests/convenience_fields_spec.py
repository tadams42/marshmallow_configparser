class DescribeConfigString(object):
    def it_uses_field_default_if_option_is_blank_in_file(
        self, config_string_config_schema, string_option_is_blank_file
    ):
        data, errors = config_string_config_schema.load(
            string_option_is_blank_file
        )

        assert not errors
        assert (
            data['STRING_WITH_DEFAULT'] ==
            config_string_config_schema.declared_fields[
                'STRING_WITH_DEFAULT'
            ].default
        )
        assert data['STRING_WITHOUT_DEFAULT'] is ''

    def it_emits_field_even_if_option_doesnt_exist_in_file(
        self, config_string_config_schema, string_option_doesnt_exist_file
    ):
        data, errors = config_string_config_schema.load(
            string_option_doesnt_exist_file
        )
        assert not errors
        assert 'STRING_WITH_DEFAULT' in data
        assert 'STRING_WITHOUT_DEFAULT' in data


class DescribeConfigInteger(object):
    def it_uses_field_default_if_option_is_blank_in_file(
        self, config_integer_config_schema, integer_option_is_blank_file
    ):
        data, errors = config_integer_config_schema.load(
            integer_option_is_blank_file
        )

        assert not errors
        assert (
            data['INTEGER_WITH_DEFAULT'] ==
            config_integer_config_schema.declared_fields[
                'INTEGER_WITH_DEFAULT'
            ].default
        )
        assert data['INTEGER_WITHOUT_DEFAULT'] is None

    def it_emits_field_even_if_option_doesnt_exist_in_file(
        self, config_integer_config_schema, integer_option_doesnt_exist_file
    ):
        data, errors = config_integer_config_schema.load(
            integer_option_doesnt_exist_file
        )
        assert not errors
        assert 'INTEGER_WITH_DEFAULT' in data
        assert 'INTEGER_WITHOUT_DEFAULT' in data

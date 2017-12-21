from rest_framework import serializers
from bank.models import Branch, Bank


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        exclude = ()

class BranchSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)
    class Meta:
        model = Branch
        exclude = ()

class BranchListSerializer(serializers.ModelSerializer):
    bank = serializers.SerializerMethodField()
    class Meta:
        model = Branch
        exclude = ()

    def get_bank(self, obj):
        return obj.bank.name

from django import forms


class BootstrapForm(forms.Form):
    # 保存排除在统一样式之外的字段
    bootstrap_exclude_fields = []

    # 给ModelForm的控件添加bootstrap样式
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue  # 在排除列表里面的字段不需要统一样式
            if field.widget.attrs:  # 有属性需要保留原来的,加上新的
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:  # 如果没有就给他直接赋值
                field.widget.attrs = {"class": "form-control", "placeholder": field.label}


class BootstrapModelForm(forms.ModelForm):
    # 保存排除在统一样式之外的字段
    bootstrap_exclude_fields = []

    # 给ModelForm的控件添加bootstrap样式
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue  # 在排除列表里面的字段不需要统一样式
            if field.widget.attrs:  # 有属性需要保留原来的,加上新的
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:  # 如果没有就给他直接赋值
                field.widget.attrs = {"class": "form-control", "placeholder": field.label}

from privileges_admin import Admin

me = Admin("Niclas", "Behrendt", "30", "hamburg")

me.privileges.privileges = ["create user", "delete user", "ban user", "restore user"]

me.greet_user()
me.describe_user()

me.privileges.show_privileges()
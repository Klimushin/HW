class Element():
    melting_temp = 0
    boiling_temp = 0

    def convert(self, t, scale):
        if str(scale) == "F":
            t += 273
            return t
        else:
            return t

    def agg_state(self, t, scale):
        t = self.convert(t, scale)
        if t < self.melting_temp:
            return f"It's solid!"
        elif t > self.boiling_temp:
            return f"It's gas!"
        else:
            return f"It's liquid!"


class Iron(Element):
    melting_temp = 1538
    boiling_temp = 2862


iron = Iron()
print(iron.agg_state(2861, "F"))
print(iron.agg_state(2861, "C"))
print(iron.agg_state(1800, "F"))
print(iron.agg_state(1800, "C"))
print(iron.agg_state(1200, "F"))
print(iron.agg_state(1200, "C"))

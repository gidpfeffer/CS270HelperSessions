
tree = {
	# Indicates whether the coin was actually heads or tails
	"H": {
		# indicates whether P1 claims heads or tails
		"H": {
			# indicates whether P2 disputes or agrees
			"A": 0.5,
			"D": 1
		},
		"T": {
			"A": -0.5,
			"D": -1
		}
	},
	"T": {
		"H": {
			"A": 0.5,
			"D": -1
		},
		"T": {
			"A": -0.5,
			"D": 1
		}
	}
}

# possible strategies
row = ["HH", "HT", "TH", "TT"]
col = ["AA", "AD", "DA", "DD"]

#iterate through all to get each cell in the matrix
for rs in row:
	whenHead = rs[0]
	whenTail = rs[1]
	for cs in col:
		whenClaimedHead = cs[0]
		whenClaimedTail = cs[1]
		whenHeadDrawn = tree["H"][whenHead][whenClaimedHead] if whenHead == "H" else tree["H"][whenHead][whenClaimedTail]
		whenTailDrawn = tree["T"][whenTail][whenClaimedHead] if whenTail == "H" else tree["T"][whenTail][whenClaimedTail]
		# half the time heads is flipped, half tails
		print(f"({rs},{cs}): {0.5 * whenHeadDrawn + 0.5 * whenTailDrawn}")
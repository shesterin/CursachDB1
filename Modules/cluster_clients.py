from sklearn.mixture import GaussianMixture

def cluster_clients(data):
    gmm = GaussianMixture(n_components=3, random_state=42)
    gmm.fit(data)
    return gmm.predict(data)

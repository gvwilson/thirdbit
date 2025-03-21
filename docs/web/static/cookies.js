function clearCookies() {
    console.log('clearing cookies');
    document.cookie.split(';').forEach(cookie => {
        const eqPos = cookie.indexOf('=');
        const name = eqPos > -1 ? cookie.substring(0, eqPos) : cookie;
        document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:00 GMT';
    });
    console.log(`cleared cookie is ${document.cookie}`);
}

function getCookie(key) {
    return Object.fromEntries(document.cookie.split('; ').map(c => c.split('=')))[key];
}

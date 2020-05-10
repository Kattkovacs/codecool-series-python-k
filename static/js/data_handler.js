// export let dataHandler = {
//     api_post: function (url, data, callback) {
//         fetch(url, {
//             method: 'POST',
//             headers:
//                 {
//                     'Accept': 'application/json',
//                     'Content-Type': 'application/json'
//                 },
//             body: JSON.stringify(data)
//         })
//             .then(response => response.json())
//             .then(data => callback(data))
//             .catch(function(error) {
//                 callback({
//
//                 });
//             });
//     }
// }